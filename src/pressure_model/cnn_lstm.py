"""
CNN-LSTM Forecaster — Risk prediction 1–5 minutes ahead
========================================================
Reference implementation using numpy (so it can run on CPU and be embedded in
tests). For production deployment on Jetson, swap to PyTorch + TensorRT.

Architecture (per docs/07_ML_Models.md):
    Input: (60 frames, 8, 8, 3 channels)
    Conv2D(8→32, k3) → ReLU → MaxPool
    Conv2D(32→64, k3) → ReLU → MaxPool
    Flatten → Dense(128) → LSTM(1, 32) → Sigmoid
"""
from __future__ import annotations
import numpy as np


def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    x = x - x.max(axis=axis, keepdims=True)
    e = np.exp(x)
    return e / e.sum(axis=axis, keepdims=True)


def relu(x: np.ndarray) -> np.ndarray:
    return np.maximum(0, x)


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-x))


def conv2d(x: np.ndarray, W: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Minimal 2D conv (stride=1, no padding) for square kernels."""
    H, W_, Cin = x.shape
    k, _, _, Cout = W.shape
    Ho, Wo = H - k + 1, W_ - k + 1
    out = np.zeros((Ho, Wo, Cout), dtype=np.float32)
    for i in range(Ho):
        for j in range(Wo):
            patch = x[i:i+k, j:j+k, :]
            out[i, j, :] = (patch[..., None] * W).sum(axis=(0, 1, 2)) + b
    return out


def maxpool2d(x: np.ndarray, k: int = 2) -> np.ndarray:
    H, W, C = x.shape
    Ho, Wo = H // k, W // k
    out = np.zeros((Ho, Wo, C), dtype=np.float32)
    for i in range(Ho):
        for j in range(Wo):
            out[i, j, :] = x[i*k:(i+1)*k, j*k:(j+1)*k, :].max(axis=(0, 1))
    return out


def dense(x: np.ndarray, W: np.ndarray, b: np.ndarray) -> np.ndarray:
    return x @ W + b


class CNNLSTM:
    """Numpy reference implementation.

    For production, replace with PyTorch nn.Module (see docs/07_ML_Models.md).
    """

    def __init__(self, seed: int = 42):
        rng = np.random.RandomState(seed)
        # CNN
        self.W1 = rng.randn(3, 3, 3, 32).astype(np.float32) * 0.1
        self.b1 = np.zeros(32, dtype=np.float32)
        self.W2 = rng.randn(3, 3, 32, 64).astype(np.float32) * 0.1
        self.b2 = np.zeros(64, dtype=np.float32)
        # After two convs on 8x8: 8-2=6, 6-2=4, after two maxpools: 4/2=2, 2/2=1 → (1,1,64)
        self.Wd = rng.randn(64, 128).astype(np.float32) * 0.1
        self.bd = np.zeros(128, dtype=np.float32)
        # LSTM: input=128, hidden=32, 4 gates (i,f,o,g)
        self.Wxh = rng.randn(128, 128).astype(np.float32) * 0.05
        self.Whh = rng.randn(32, 128).astype(np.float32) * 0.05
        self.bh  = np.zeros(128, dtype=np.float32)
        self.Wo  = rng.randn(32, 1).astype(np.float32) * 0.05
        self.bo  = np.zeros(1, dtype=np.float32)

    def forward(self, x: np.ndarray) -> float:
        """x: (60, 8, 8, 3) → scalar risk ∈ [0, 1]"""
        h = np.zeros(32, dtype=np.float32)
        c = np.zeros(32, dtype=np.float32)
        # Split LSTM weights into 4 gates
        Wxi = self.Wxh[:, 0:32];  Wxf = self.Wxh[:, 32:64]
        Wxo = self.Wxh[:, 64:96]; Wxg = self.Wxh[:, 96:128]
        Whi = self.Whh[:, 0:32];  Whf = self.Whh[:, 32:64]
        Who = self.Whh[:, 64:96]; Whg = self.Whh[:, 96:128]
        bi  = self.bh[0:32];      bf  = self.bh[32:64]
        bo  = self.bh[64:96];     bg  = self.bh[96:128]

        for t in range(x.shape[0]):
            frame = x[t]
            z = relu(conv2d(frame, self.W1, self.b1))
            z = maxpool2d(z, 2)
            z = relu(conv2d(z, self.W2, self.b2))
            z = maxpool2d(z, 1)
            z = z.reshape(-1)
            z = relu(dense(z, self.Wd, self.bd))
            # LSTM cell
            ig = sigmoid(z @ Wxi + h @ Whi + bi)
            fg = sigmoid(z @ Wxf + h @ Whf + bf)
            og = sigmoid(z @ Wxo + h @ Who + bo)
            gg = np.tanh(z @ Wxg + h @ Whg + bg)
            c = fg * c + ig * gg
            h = og * np.tanh(c)
        return float(sigmoid(h @ self.Wo + self.bo)[0])


def sacrum_weighted_mse(y_true: np.ndarray, y_pred: np.ndarray,
                        mask: np.ndarray | None = None) -> float:
    """Weighted MSE emphasizing sacrum zone (rows 3..6, cols 3..6)."""
    w = np.ones_like(y_true)
    if mask is None:
        mask = np.zeros((8, 8), dtype=np.float32)
        mask[3:6, 3:6] = 3.0
    w = w * (1 + mask)
    return float(((y_true - y_pred) ** 2 * w).mean())


if __name__ == "__main__":
    rng = np.random.RandomState(42)
    frames = np.zeros((60, 8, 8, 3), dtype=np.float32)
    frames[..., 0] = rng.rand(60, 8, 8)
    frames[..., 1] = (rng.rand(60, 8, 8) > 0.7).astype(np.float32)
    frames[..., 2] = 0.0  # supine

    model = CNNLSTM(seed=42)
    risk = model.forward(frames)
    print(f"Predicted risk (1 min ahead): {risk:.4f}")
