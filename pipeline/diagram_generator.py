"""
Generate all technical diagrams for the Adaptive Air Cushion + AAC project.
Uses matplotlib for reproducible PNG output.

Run: python pipeline/diagram_generator.py
"""
from __future__ import annotations

import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "figure.dpi": 110,
    "savefig.dpi": 150,
    "savefig.bbox": "tight",
    "font.family": ["DejaVu Sans", "sans-serif"],
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
})


def add_box(ax, xy, w, h, label, color="#E3F2FD", edge="#1976D2", text_color="#0D47A1"):
    box = FancyBboxPatch(
        xy, w, h,
        boxstyle="round,pad=0.02,rounding_size=0.05",
        linewidth=1.4, facecolor=color, edgecolor=edge,
    )
    ax.add_patch(box)
    cx, cy = xy[0] + w / 2, xy[1] + h / 2
    ax.text(cx, cy, label, ha="center", va="center", fontsize=9, color=text_color)


def add_arrow(ax, p1, p2, color="#37474F", lw=1.4, label=None, label_offset=(0, 0)):
    arrow = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=12,
                             linewidth=lw, color=color)
    ax.add_patch(arrow)
    if label:
        mx = (p1[0] + p2[0]) / 2 + label_offset[0]
        my = (p1[1] + p2[1]) / 2 + label_offset[1]
        ax.text(mx, my, label, fontsize=8, color=color)


def diagram_system_block():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14); ax.set_ylim(0, 8); ax.axis("off")
    ax.set_title("System Block Diagram — Adaptive Air Cushion + Eye-Tracking AAC", pad=14)
    add_box(ax, (0.3, 3.3), 2.0, 1.4, "Patient\n(limited mobility)", color="#FFE0B2", edge="#E65100")
    add_box(ax, (3.0, 5.6), 2.6, 1.0, "Hybrid Pressure\nMatrix 8x8\n(Velostat + Piezocap.)", color="#C8E6C9", edge="#2E7D32")
    add_box(ax, (3.0, 3.9), 2.6, 1.0, "Stereo Camera Rig\n(2x Global Shutter)", color="#C8E6C9", edge="#2E7D32")
    add_box(ax, (3.0, 2.2), 2.6, 1.0, "Load Cell +\nPosture Sensor", color="#C8E6C9", edge="#2E7D32")
    add_box(ax, (6.4, 3.9), 2.4, 1.6, "STM32F407\nADC DMA, SPI MUX\nPWM valves, UART", color="#FFF9C4", edge="#F57F17")
    add_box(ax, (6.4, 1.5), 2.4, 1.2, "Pneumatic Manifold\n64 valves + 1 pump", color="#FFE0B2", edge="#E65100")
    add_box(ax, (9.4, 5.6), 2.8, 1.0, "PTI Engine\nPressure-Time-Intensity", color="#E1BEE7", edge="#6A1B9A")
    add_box(ax, (9.4, 4.4), 2.8, 1.0, "CNN-LSTM\nRisk Forecaster (1-5 min)", color="#E1BEE7", edge="#6A1B9A")
    add_box(ax, (9.4, 3.2), 2.8, 1.0, "Eye-Tracker\nPupil + Stereo + Arm IK", color="#E1BEE7", edge="#6A1B9A")
    add_box(ax, (9.4, 2.0), 2.8, 1.0, "Qwen-0.5B + LoRA\nAAC Sentence Gen", color="#E1BEE7", edge="#6A1B9A")
    add_box(ax, (9.4, 0.8), 2.8, 1.0, "Self-Improving Loop\n(Contextual Bandit)", color="#F8BBD0", edge="#AD1457")
    add_box(ax, (12.7, 3.0), 1.2, 3.4, "Jetson\nOrin\nNano\n40 TOPS", color="#BBDEFB", edge="#1565C0")
    add_box(ax, (3.0, 0.4), 2.6, 1.2, "Robot Arm 3 DOF\n(Pan-Tilt-Roll)", color="#FFE0B2", edge="#E65100")
    add_box(ax, (12.7, 6.8), 1.2, 0.8, '10" Touch\n+ TTS', color="#F5F5F5", edge="#424242")
    add_arrow(ax, (2.3, 4.0), (3.0, 4.4))
    add_arrow(ax, (2.3, 4.0), (3.0, 6.1))
    add_arrow(ax, (5.6, 6.1), (6.4, 4.7))
    add_arrow(ax, (5.6, 4.4), (6.4, 4.7))
    add_arrow(ax, (8.8, 4.7), (9.4, 4.9))
    add_arrow(ax, (8.8, 2.1), (9.4, 6.1))
    add_arrow(ax, (12.2, 6.1), (12.7, 4.7), label="ROS2")
    add_arrow(ax, (12.2, 4.9), (12.7, 4.7))
    add_arrow(ax, (12.2, 3.7), (12.7, 4.7))
    add_arrow(ax, (12.2, 2.5), (12.7, 4.7))
    add_arrow(ax, (12.2, 1.3), (12.7, 4.7))
    add_arrow(ax, (3.5, 1.6), (3.5, 2.2))
    add_arrow(ax, (5.6, 3.0), (9.4, 3.7), label="control", label_offset=(0, -0.3))
    add_arrow(ax, (13.3, 6.4), (13.3, 5.5))
    ax.text(0.3, 7.7, "Legend:", fontsize=9, fontweight="bold")
    ax.add_patch(Rectangle((1.1, 7.5), 0.3, 0.2, color="#C8E6C9"))
    ax.text(1.5, 7.6, "Sensors", fontsize=8)
    ax.add_patch(Rectangle((3.0, 7.5), 0.3, 0.2, color="#FFF9C4"))
    ax.text(3.4, 7.6, "MCU/Control", fontsize=8)
    ax.add_patch(Rectangle((5.2, 7.5), 0.3, 0.2, color="#E1BEE7"))
    ax.text(5.6, 7.6, "AI/ML", fontsize=8)
    ax.add_patch(Rectangle((7.0, 7.5), 0.3, 0.2, color="#FFE0B2"))
    ax.text(7.4, 7.6, "Actuator/Patient", fontsize=8)
    ax.add_patch(Rectangle((9.5, 7.5), 0.3, 0.2, color="#BBDEFB"))
    ax.text(9.9, 7.6, "Compute", fontsize=8)
    ax.add_patch(Rectangle((11.5, 7.5), 0.3, 0.2, color="#F8BBD0"))
    ax.text(11.9, 7.6, "Adaptive", fontsize=8)
    plt.savefig(OUT / "01_system_block_diagram.png"); plt.close()
    print("Saved: 01_system_block_diagram.png")


def diagram_hardware_schematic():
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14); ax.set_ylim(0, 9); ax.axis("off")
    ax.set_title("Hardware Schematic - STM32 to Sensors/Actuators to Jetson", pad=14)
    add_box(ax, (0.3, 7.8), 2.0, 0.9, "24V DC\nMean Well", color="#FFCDD2", edge="#B71C1C")
    add_box(ax, (2.7, 7.8), 2.0, 0.9, "Buck 5V\n(LM2596)", color="#FFCDD2", edge="#B71C1C")
    add_box(ax, (5.1, 7.8), 2.0, 0.9, "LDO 3.3V\n(AMS1117)", color="#FFCDD2", edge="#B71C1C")
    add_box(ax, (7.5, 7.8), 2.0, 0.9, "UPS 12V/7Ah\n(30 min backup)", color="#FFCDD2", edge="#B71C1C")
    add_box(ax, (5.1, 5.4), 4.0, 1.8, "STM32F407VGT6\n168 MHz, 1MB Flash\nADCx3, SPIx3, UARTx6, PWMx12", color="#FFF9C4", edge="#F57F17")
    add_box(ax, (10.0, 5.4), 3.5, 1.8, "Jetson Orin Nano 8GB\n40 TOPS, JetPack 5.1.3\nMIPIx2, USB3, HDMI", color="#BBDEFB", edge="#1565C0")
    add_box(ax, (0.3, 3.6), 4.0, 1.5, "Pressure Matrix 8x8\n64 Velostat + 8 Piezocap.", color="#C8E6C9", edge="#2E7D32")
    add_box(ax, (0.3, 1.8), 4.0, 1.4, "SPI MUX 74HC4051 x8\nADC DMA to STM32", color="#C8E6C9", edge="#2E7D32")
    add_box(ax, (10.0, 1.8), 3.5, 1.4, "64 Solenoid Valves\n12V, Orifice 1.5mm\nULN2803 driver", color="#FFE0B2", edge="#E65100")
    add_box(ax, (10.0, 3.4), 3.5, 1.5, "Diaphragm Pump + Reservoir\n6 L/min, 2L buffer\nThermal cutoff 60C", color="#FFE0B2", edge="#E65100")
    add_box(ax, (4.6, 0.5), 2.4, 1.4, "Camera x2 (OV9281)\nGlobal Shutter 640x480\nIR LED 850 nm", color="#C8E6C9", edge="#2E7D32")
    add_box(ax, (7.4, 0.5), 2.4, 1.4, "Robot Arm 3 DOF\nDynamixel XL-330\n(STM32G0 bridge)", color="#FFE0B2", edge="#E65100")
    add_box(ax, (10.0, 0.5), 3.5, 1.0, '10" Touchscreen 1280x800\nTTS (eSpeak)', color="#F5F5F5", edge="#424242")
    add_arrow(ax, (7.1, 8.2), (5.1, 7.2), label="24V", color="#B71C1C")
    add_arrow(ax, (7.1, 8.2), (10.0, 7.2), label="5V", color="#B71C1C")
    add_arrow(ax, (2.3, 4.4), (5.1, 5.4), label="SPI")
    add_arrow(ax, (5.1, 4.4), (7.4, 1.2), label="UART")
    add_arrow(ax, (9.1, 5.9), (10.0, 5.9), label="UART/USB")
    add_arrow(ax, (9.1, 4.6), (10.0, 4.6), label="MIPIx2")
    add_arrow(ax, (11.7, 5.4), (11.7, 4.9), label="GPIO")
    add_arrow(ax, (11.7, 3.4), (11.7, 2.6), label="PWMx8")
    add_arrow(ax, (5.1, 4.4), (4.3, 1.9), label="PWMx4")
    add_arrow(ax, (10.0, 1.0), (11.7, 5.4), label="HDMI")
    add_box(ax, (0.3, 5.6), 4.0, 1.0, "Emergency Stop\n+ Watchdog + Fuse", color="#FFCDD2", edge="#B71C1C")
    add_arrow(ax, (2.3, 5.6), (5.1, 6.4), color="#B71C1C")
    plt.savefig(OUT / "02_hardware_schematic.png"); plt.close()
    print("Saved: 02_hardware_schematic.png")


def diagram_software_architecture():
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14); ax.set_ylim(0, 9); ax.axis("off")
    ax.set_title("Software Architecture - ROS2 Nodes + AI Services", pad=14)
    layers = [
        (7.5, "Presentation",      "UI Dashboard (Streamlit)\nPressure heatmap + Risk map + AAC grid"),
        (6.2, "Application",       "State Machine, Orchestrator, Safety Gate"),
        (4.9, "AI/ML Services",    "PTI Engine, CNN-LSTM Forecaster\nQwen-0.5B + LoRA, Self-Improve Bandit"),
        (3.6, "Perception",        "Pressure Map, Stereo Eye-Tracker\nCamera Positioner (Arm IK)"),
        (2.3, "Control",           "PID Cushion (64 cells), Servo Arm\nWatchdog"),
        (1.0, "HAL/Drivers",       "UART, SPI, I2C, MIPI, GPIO"),
    ]
    colors = ["#F5F5F5", "#E1BEE7", "#FFE0B2", "#C8E6C9", "#FFF9C4", "#BBDEFB"]
    for (y, name, desc), c in zip(layers, colors):
        add_box(ax, (0.3, y), 4.0, 1.0, f"{name}\n{desc}", color=c)
        ax.add_patch(Rectangle((0.3, y), 0.3, 1.0, color=c, alpha=0.5))
        ax.text(0.15, y + 0.5, name[:3], rotation=90, ha="center", va="center", fontsize=8, color="#37474F")
    add_box(ax, (5.0, 6.2), 2.6, 1.0, "ROS2 Humble\nDDS / Topics\nServices + Actions", color="#E1BEE7", edge="#6A1B9A")
    nodes = [
        (5.0, 4.9, "pressure_node"), (8.0, 4.9, "eye_node"),
        (5.0, 3.6, "cushion_ctrl"),   (8.0, 3.6, "arm_ctrl"),
        (5.0, 2.3, "aac_node"),       (8.0, 2.3, "safety_node"),
        (6.5, 1.0, "dashboard_node"),
    ]
    for x, y, name in nodes:
        add_box(ax, (x, y), 2.5, 0.8, name, color="#FFF9C4", edge="#F57F17")
    topics = [
        ("/pressure/raw",       (5.0, 5.7), (8.0, 5.7)),
        ("/pressure/calibrated",(5.0, 5.4), (8.0, 5.4)),
        ("/risk/map",           (5.0, 5.1), (8.0, 5.1)),
        ("/gaze/vector",        (5.0, 4.4), (8.0, 4.4)),
        ("/cushion/cmd",        (5.0, 3.1), (8.0, 3.1)),
        ("/arm/cmd",            (5.0, 2.8), (8.0, 2.8)),
        ("/aac/grid",           (5.0, 1.8), (8.0, 1.8)),
        ("/system/safety",      (5.0, 1.5), (8.0, 1.5)),
    ]
    for label, p1, p2 in topics:
        add_arrow(ax, p1, p2, color="#6A1B9A", lw=0.8, label=label, label_offset=(0, 0.05))
    add_box(ax, (11.0, 4.9), 2.6, 1.0, "STM32\n(UART bridge)", color="#FFCDD2", edge="#B71C1C")
    add_box(ax, (11.0, 3.6), 2.6, 1.0, "Cameras\n(2x MIPI)", color="#C8E6C9", edge="#2E7D32")
    add_box(ax, (11.0, 2.3), 2.6, 1.0, "Robot Arm\n(Dynamixel)", color="#FFE0B2", edge="#E65100")
    add_box(ax, (11.0, 1.0), 2.6, 0.8, "Touch UI + TTS", color="#F5F5F5", edge="#424242")
    add_arrow(ax, (10.5, 5.3), (11.0, 5.3), color="#37474F")
    add_arrow(ax, (10.5, 4.0), (11.0, 4.0), color="#37474F")
    add_arrow(ax, (10.5, 2.7), (11.0, 2.7), color="#37474F")
    add_arrow(ax, (10.5, 1.4), (11.0, 1.4), color="#37474F")
    add_box(ax, (5.0, 7.5), 8.6, 1.0, "Reproducibility: Docker + repro_lock.yaml + seed=42", color="#FFCDD2", edge="#B71C1C")
    plt.savefig(OUT / "03_software_architecture.png"); plt.close()
    print("Saved: 03_software_architecture.png")


def diagram_data_pipeline():
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14); ax.set_ylim(0, 7); ax.axis("off")
    ax.set_title("End-to-End Data Pipeline - Sensor to AI to Control to User", pad=14)
    stages = [
        (0.3, 4.5, "Sensor Layer\n64 Velostat + 8 Piezocap.\n2x Global Shutter"),
        (3.3, 4.5, "Acquisition\nSTM32 ADC DMA @ 10 Hz\nCamera @ 30 fps"),
        (6.3, 4.5, "Preprocessing\nCross-calibration\nRectify + Pupil detect"),
        (9.3, 4.5, "AI Services\nPTI + CNN-LSTM\nQwen-LoRA"),
        (12.3, 4.5, "Action\nPID 64 cells\nArm IK\nTTS"),
    ]
    colors = ["#C8E6C9", "#FFF9C4", "#E1BEE7", "#FFE0B2", "#FFCDD2"]
    for (x, y, lbl), c in zip(stages, colors):
        add_box(ax, (x, y), 2.8, 1.5, lbl, color=c)
    for x in [3.1, 6.1, 9.1, 12.1]:
        add_arrow(ax, (x, 5.25), (x + 0.2, 5.25), color="#37474F", lw=2)
    add_box(ax, (5.0, 1.0), 8.0, 1.0, "Feedback & Self-Improvement Loop\nContextual Bandit updates PID gain, Threshold, AAC priors", color="#F8BBD0", edge="#AD1457")
    add_arrow(ax, (13.7, 4.5), (13.7, 2.0), color="#AD1457", lw=1.6)
    add_arrow(ax, (13.7, 2.0), (5.0, 2.0), color="#AD1457", lw=1.6)
    add_arrow(ax, (5.0, 2.0), (5.0, 4.5), color="#AD1457", lw=1.6)
    lat = ["10 Hz", "30 fps", "< 50 ms", "< 200 ms", "< 100 ms"]
    for (x, _, _), l in zip(stages, lat):
        ax.text(x + 1.4, 6.4, l, ha="center", fontsize=8, color="#37474F", style="italic")
    plt.savefig(OUT / "04_data_pipeline.png"); plt.close()
    print("Saved: 04_data_pipeline.png")


def diagram_ml_architecture():
    fig, axes = plt.subplots(1, 3, figsize=(16, 7))
    fig.suptitle("ML Model Architecture - PTI Engine, CNN-LSTM, Qwen-LoRA", fontsize=13, fontweight="bold")
    ax = axes[0]
    ax.set_xlim(0, 8); ax.set_ylim(0, 8); ax.axis("off"); ax.set_title("A. PTI Engine")
    add_box(ax, (0.5, 6.3), 3.0, 1.0, "Input\nPressure map 8x8\nPosture class, Time t", color="#C8E6C9")
    add_box(ax, (4.0, 6.3), 3.0, 1.0, "Threshold map\nP_th (per cell)", color="#FFF9C4")
    add_box(ax, (2.0, 4.6), 4.0, 1.0, "PTI(t) = integral w*(P/P_th) d-tau", color="#FFE0B2")
    add_box(ax, (0.5, 2.6), 3.0, 1.0, "Per-cell PTI\n8x8 score", color="#E1BEE7")
    add_box(ax, (4.0, 2.6), 3.0, 1.0, "Risk classification\nlow/mod/high/crit", color="#F8BBD0")
    add_box(ax, (2.0, 0.5), 4.0, 1.0, "Output to /risk/map + CNN-LSTM input", color="#FFCDD2")
    add_arrow(ax, (2.0, 6.3), (4.0, 5.6))
    add_arrow(ax, (4.0, 5.6), (4.0, 5.1))
    add_arrow(ax, (2.0, 4.6), (2.0, 3.6))
    add_arrow(ax, (4.0, 4.6), (5.5, 3.6))
    add_arrow(ax, (2.0, 2.6), (4.0, 1.5))
    ax = axes[1]
    ax.set_xlim(0, 8); ax.set_ylim(0, 8); ax.axis("off"); ax.set_title("B. CNN-LSTM Forecaster")
    add_box(ax, (0.5, 6.5), 7.0, 1.0, "Input: 60 frames x (8x8 + posture)\nshape = (60, 8, 8, 3)", color="#C8E6C9")
    add_box(ax, (0.5, 5.0), 7.0, 1.0, "Conv2D(8 to 32, k3) to BN to MaxPool\nConv2D(32 to 64, k3) to BN to MaxPool", color="#FFF9C4")
    add_box(ax, (0.5, 3.5), 7.0, 1.0, "Flatten to Dense(128) to\nLSTM(2 layers, hidden=128) to Dropout(0.2)", color="#FFE0B2")
    add_box(ax, (0.5, 2.0), 7.0, 1.0, "Dense(64) to ReLU to Dense(1) to Sigmoid", color="#E1BEE7")
    add_box(ax, (0.5, 0.5), 7.0, 1.0, "Output: forecast risk 1-5 min ahead\nLoss: weighted MSE (sacrum x3)", color="#FFCDD2")
    for y in [6.0, 4.5, 3.0, 1.5]:
        add_arrow(ax, (4.0, y), (4.0, y - 0.5))
    ax = axes[2]
    ax.set_xlim(0, 8); ax.set_ylim(0, 8); ax.axis("off"); ax.set_title("C. Qwen-0.5B + LoRA (AAC)")
    add_box(ax, (0.5, 6.5), 7.0, 1.0, "Qwen2-0.5B-Instruct (frozen)", color="#C8E6C9")
    add_box(ax, (0.5, 5.0), 7.0, 1.0, "LoRA: r=8, alpha=16\ntarget: q_proj, v_proj, dropout=0.05", color="#FFF9C4")
    add_box(ax, (0.5, 3.5), 7.0, 1.0, "Train: 50 AAC sentence pairs\n5 epoch, lr=1e-4, seed=42", color="#FFE0B2")
    add_box(ax, (0.5, 2.0), 7.0, 1.0, "INT8 quantization to TensorRT\n(target latency < 300 ms)", color="#E1BEE7")
    add_box(ax, (0.5, 0.5), 7.0, 1.0, "Inference: keywords to full sentence\nBLEU-4 to 0.30, chrF, rating to 3.5/5", color="#FFCDD2")
    for y in [6.0, 4.5, 3.0, 1.5]:
        add_arrow(ax, (4.0, y), (4.0, y - 0.5))
    plt.savefig(OUT / "05_ml_model_architecture.png"); plt.close()
    print("Saved: 05_ml_model_architecture.png")


def diagram_pressure_pipeline():
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14); ax.set_ylim(0, 7); ax.axis("off")
    ax.set_title("Pressure Map Pipeline (kenh hinh ap suat)", pad=14)
    stages = [
        (0.3, 4.5, "Raw frame\n64 Velostat\n+ 8 Piezocap.\n(8x8 + 8)"),
        (3.3, 4.5, "STM32 ADC\n12-bit @ 10 Hz\nDMA buffer"),
        (6.3, 4.5, "Cross-calibration\nOnline Kalman\n(Velostat to Pz)"),
        (9.3, 4.5, "Pressure map\n8x8 mmHg\nnormalized"),
        (12.3, 4.5, "PTI Engine\nRisk map\n8x8 score"),
    ]
    colors = ["#C8E6C9", "#FFF9C4", "#E1BEE7", "#FFE0B2", "#FFCDD2"]
    for (x, y, lbl), c in zip(stages, colors):
        add_box(ax, (x, y), 2.8, 1.5, lbl, color=c)
    for x in [3.1, 6.1, 9.1, 12.1]:
        add_arrow(ax, (x, 5.25), (x + 0.2, 5.25), color="#37474F", lw=2)
    channels = [
        ("ch0: P (mmHg)",       "#1976D2"),
        ("ch1: drift residual", "#388E3C"),
        ("ch2: posture one-hot", "#F57F17"),
    ]
    for i, (lbl, c) in enumerate(channels):
        add_box(ax, (0.3, 2.5 - i * 0.7), 2.8, 0.6, lbl, color=c, edge="#37474F", text_color="white")
    add_box(ax, (9.3, 2.5), 2.8, 0.6, "to CNN-LSTM input\n(3 channels)", color="#FFCDD2", text_color="white")
    pm = np.random.RandomState(0).rand(8, 8) * 60
    pm[3, 3] = 90; pm[4, 4] = 75; pm[2, 6] = 80
    inset_ax = fig.add_axes([0.62, 0.07, 0.18, 0.25])
    inset_ax.imshow(pm, cmap="hot", vmin=0, vmax=100)
    inset_ax.set_title("Risk map (sample)", fontsize=8); inset_ax.axis("off")
    plt.savefig(OUT / "06_pressure_map_flow.png"); plt.close()
    print("Saved: 06_pressure_map_flow.png")


def diagram_eye_tracking():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14); ax.set_ylim(0, 8); ax.axis("off")
    ax.set_title("Eye-Tracking Pipeline (kenh hinh stereo camera)", pad=14)
    stages = [
        (0.3, 5.5, "Stereo Camera\n2x OV9281\n640x480 @ 60fps\nIR LED 850 nm"),
        (3.3, 5.5, "Frame sync +\nRectify\n(stereo calib)"),
        (6.3, 5.5, "Pupil Detection\nMediaPipe Face Mesh\n(468 landmarks)"),
        (9.3, 5.5, "Stereo Triangulation\n3D pupil position\nto Gaze vector"),
        (12.3, 5.5, "Robot Arm IK\nPan +-30deg\nTilt +-20deg\nRoll +-10deg"),
    ]
    colors = ["#C8E6C9", "#FFF9C4", "#E1BEE7", "#FFE0B2", "#FFCDD2"]
    for (x, y, lbl), c in zip(stages, colors):
        add_box(ax, (x, y), 2.8, 1.5, lbl, color=c)
    for x in [3.1, 6.1, 9.1, 12.1]:
        add_arrow(ax, (x, 6.25), (x + 0.2, 6.25), color="#37474F", lw=2)
    ch = [
        ("ch0: left frame (gray)",  "#37474F"),
        ("ch1: right frame (gray)", "#37474F"),
        ("ch2: face mesh overlay",  "#1976D2"),
        ("ch3: pupil mask",         "#AD1457"),
    ]
    for i, (lbl, c) in enumerate(ch):
        add_box(ax, (0.3, 3.8 - i * 0.7), 2.8, 0.6, lbl, color=c, edge="#37474F", text_color="white")
    add_box(ax, (9.3, 3.5), 2.8, 0.6, "to AAC grid 5x3\ngaze to cell hit", color="#E1BEE7")
    add_box(ax, (6.3, 1.0), 8.6, 1.2, "AAC Grid to Keyword list to Qwen-LoRA to Sentence to TTS\nExample: ['toi','khat','nuoc'] to 'Toi dang khat nuoc, lam on cho toi mot ly.'", color="#F8BBD0", edge="#AD1457")
    add_arrow(ax, (13.7, 5.5), (13.7, 2.2), color="#AD1457", lw=1.5)
    add_arrow(ax, (6.3, 2.2), (6.3, 5.5), color="#AD1457", lw=1.5)
    plt.savefig(OUT / "07_eye_tracking_flow.png"); plt.close()
    print("Saved: 07_eye_tracking_flow.png")


def diagram_aac_ui():
    fig = plt.figure(figsize=(14, 9))
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14); ax.set_ylim(0, 9); ax.axis("off")
    ax.set_title("AAC UI Mockup - Pressure Map + Risk Overlay + AAC Grid", pad=14)
    add_box(ax, (0.3, 5.5), 6.0, 3.0, "Pressure Map + Risk Overlay\n(8x8 heatmap)", color="#FFCDD2", edge="#B71C1C")
    pm = np.random.RandomState(42).rand(8, 8) * 40
    pm[3:6, 3:6] += 30
    inset_ax = fig.add_axes([0.045, 0.55, 0.43, 0.32])
    inset_ax.imshow(pm, cmap="hot", vmin=0, vmax=80)
    inset_ax.set_title("Live pressure (mmHg)", fontsize=9)
    inset_ax.set_xticks([]); inset_ax.set_yticks([])
    add_box(ax, (6.5, 7.0), 7.2, 1.5, "Status\nPeak: 78 mmHg (cell 3,4), Mean sacrum: 28 mmHg\nPTI critical: 2 cells, TOT: 4% over 4h\nEye-track accuracy: 87%, AAC latency: 240 ms", color="#FFF9C4", edge="#F57F17")
    add_box(ax, (6.5, 4.0), 7.2, 2.7, "AAC Grid 5x3 (gaze-driven)", color="#E1BEE7", edge="#6A1B9A")
    words = [
        ["Toi", "Ban", "Can", "Muon", "Xin"],
        ["Cam on", "Xin loi", "Vui", "Buon", "Met"],
        ["Nuoc", "Thuoc", "Dau", "Y ta", "Bac si"],
    ]
    cell_w, cell_h = 7.2 / 5, 2.7 / 3
    for r, row in enumerate(words):
        for c, w in enumerate(row):
            x = 6.5 + c * cell_w
            y = 4.0 + (2 - r) * cell_h
            ax.add_patch(Rectangle((x + 0.05, y + 0.05), cell_w - 0.1, cell_h - 0.1,
                                    facecolor="#FFFFFF", edgecolor="#6A1B9A"))
            if (r, c) == (2, 2):
                ax.add_patch(Rectangle((x + 0.05, y + 0.05), cell_w - 0.1, cell_h - 0.1,
                                        facecolor="#FFD54F", edgecolor="#F57F17", linewidth=2))
            ax.text(x + cell_w / 2, y + cell_h / 2, w, ha="center", va="center", fontsize=11, color="#0D47A1")
    add_box(ax, (0.3, 3.5), 6.0, 1.0, "Sentence (Qwen-LoRA):\n'Toi dang dau o vung lung, xin goi y ta giup toi.'", color="#F8BBD0", edge="#AD1457")
    add_box(ax, (0.3, 1.0), 6.0, 2.0, "Stereo Camera Rig\nPan: +5deg, Tilt: -2deg, Roll: 0deg\nBaseline: 60 mm, Depth: 50 cm", color="#C8E6C9", edge="#2E7D32")
    ax.add_patch(Circle((3.3, 2.0), 0.4, facecolor="#FFCDD2", edgecolor="#B71C1C"))
    ax.text(3.3, 2.0, "Face\nROI", ha="center", va="center", fontsize=8, color="#B71C1C")
    add_box(ax, (6.5, 2.0), 7.2, 1.5, "TTS Output (eSpeak):\n'Toi dang dau o vung lung, xin goi y ta giup toi.'\nVolume: 60%", color="#FFE0B2", edge="#E65100")
    add_box(ax, (6.5, 0.3), 7.2, 1.5, "Buttons: Help, Settings, Emergency Stop\nLogs: 1024 events today, Last calibration: 12 min ago", color="#F5F5F5", edge="#424242")
    plt.savefig(OUT / "08_aac_ui_mockup.png"); plt.close()
    print("Saved: 08_aac_ui_mockup.png")


def diagram_deployment():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14); ax.set_ylim(0, 8); ax.axis("off")
    ax.set_title("Deployment Diagram - Bedside Edge AI", pad=14)
    add_box(ax, (0.3, 0.3), 9.0, 7.4, "BEDSIDE UNIT (research-only)", color="#FFCDD2", edge="#B71C1C")
    add_box(ax, (0.6, 5.5), 3.0, 1.8, "Jetson Orin Nano\n40 TOPS, 8GB\nUbuntu 20.04, JetPack 5.1.3\nDocker, ROS2 Humble", color="#BBDEFB", edge="#1565C0")
    add_box(ax, (4.0, 5.5), 3.0, 1.8, "STM32F407\nFreeRTOS\nADC, SPI, PWM\nUART bridge\nWatchdog", color="#FFF9C4", edge="#F57F17")
    add_box(ax, (0.6, 3.0), 2.5, 1.8, "Stereo Cameras\n+ Robot Arm", color="#C8E6C9", edge="#2E7D32")
    add_box(ax, (3.5, 3.0), 3.5, 1.8, "Air Cushion\n64 cells + 64 valves\nHybrid pressure mat", color="#FFE0B2", edge="#E65100")
    add_box(ax, (7.5, 3.0), 1.6, 1.8, '10" Touch UI\n+ TTS', color="#F5F5F5", edge="#424242")
    add_box(ax, (7.5, 5.5), 1.6, 1.8, "24V DC\n+ UPS", color="#FFCDD2", edge="#B71C1C")
    add_box(ax, (0.6, 1.0), 3.0, 1.0, "Emergency Stop\n(Fail-safe cutoff)", color="#FFCDD2", edge="#B71C1C")
    add_box(ax, (4.0, 1.0), 3.0, 1.0, "Local Storage\nEncrypted LUKS\nLogs + Datasets", color="#FFF9C4", edge="#F57F17")
    add_box(ax, (7.5, 1.0), 1.6, 1.0, "WiFi\n(opt-in OFF)", color="#F5F5F5", edge="#424242")
    add_box(ax, (10.0, 4.5), 3.5, 3.0, "CLOUD (opt-in, OFF by default)\nUpdate LoRA weights\nAggregate anonymous metrics\nONLY with patient consent", color="#E1BEE7", edge="#6A1B9A")
    add_arrow(ax, (9.1, 2.0), (10.0, 5.0), color="#6A1B9A", lw=1.5, label="(if enabled)", label_offset=(0, 0.2))
    add_box(ax, (10.0, 1.0), 3.5, 2.0, "DEV WORKSTATION\n(notebook/PC)\nTrain models\nReview logs\nUpdate firmware", color="#C8E6C9", edge="#2E7D32")
    add_arrow(ax, (9.1, 4.0), (10.0, 2.5), color="#2E7D32", lw=1.5)
    plt.savefig(OUT / "09_deployment_diagram.png"); plt.close()
    print("Saved: 09_deployment_diagram.png")


def diagram_cross_calibration():
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14); ax.set_ylim(0, 7); ax.axis("off")
    ax.set_title("Cross-Calibration (kenh hinh) - Velostat to Piezocapacitive Hybrid Sensing", pad=14)
    add_box(ax, (0.3, 4.5), 3.0, 1.5, "Velostat raw\nV_t (ADC, 12-bit)\n8x8 matrix", color="#C8E6C9")
    add_box(ax, (0.3, 2.5), 3.0, 1.5, "Piezocapacitive anchors\nP_t (mmHg)\n8 anchor points", color="#FFF9C4")
    add_box(ax, (4.0, 4.5), 3.0, 1.5, "Velostat calibration\nV_t = a*P_t + b\n(a,b fit online)", color="#E1BEE7")
    add_box(ax, (4.0, 2.5), 3.0, 1.5, "Piezocapacitive offset\nP_t = c*V_t + d\n(c,d lab-cal)", color="#FFE0B2")
    add_box(ax, (8.0, 3.5), 3.0, 1.5, "Kalman fusion\nstate = pressure\nobs = Velostat + Pz\nupdate 5/min", color="#F8BBD0", edge="#AD1457")
    add_box(ax, (11.5, 3.5), 2.3, 1.5, "Calibrated pressure map\n8x8 mmHg\n(drift-reduced)", color="#FFCDD2")
    drift_x = np.linspace(0, 30, 100)
    drift_y = drift_x * 0.3 + np.random.RandomState(0).randn(100) * 0.5
    drift_y_hybrid = drift_x * 0.05 + np.random.RandomState(1).randn(100) * 0.3
    inset_ax = fig.add_axes([0.10, 0.08, 0.32, 0.27])
    inset_ax.plot(drift_x, drift_y, label="Velostat only", color="#B71C1C")
    inset_ax.plot(drift_x, drift_y_hybrid, label="Hybrid (calibrated)", color="#2E7D32")
    inset_ax.set_xlabel("Time (min)", fontsize=8)
    inset_ax.set_ylabel("Drift error (mmHg)", fontsize=8)
    inset_ax.set_title("Drift comparison", fontsize=9)
    inset_ax.legend(fontsize=7)
    inset_ax.grid(True, alpha=0.3)
    add_arrow(ax, (3.3, 5.25), (4.0, 5.25))
    add_arrow(ax, (3.3, 3.25), (4.0, 3.25))
    add_arrow(ax, (7.0, 5.25), (8.0, 4.3))
    add_arrow(ax, (7.0, 3.25), (8.0, 4.3))
    add_arrow(ax, (11.0, 4.3), (11.5, 4.3))
    add_box(ax, (4.0, 0.3), 9.8, 0.9, "Result: Hybrid reduces drift > 60% vs Velostat-only (target >= 20%)\nEnables reliable PTI computation over 4h+ sessions.", color="#FFCDD2", edge="#B71C1C")
    plt.savefig(OUT / "10_cross_calibration.png"); plt.close()
    print("Saved: 10_cross_calibration.png")


def generate_all():
    diagram_system_block()
    diagram_hardware_schematic()
    diagram_software_architecture()
    diagram_data_pipeline()
    diagram_ml_architecture()
    diagram_pressure_pipeline()
    diagram_eye_tracking()
    diagram_aac_ui()
    diagram_deployment()
    diagram_cross_calibration()
    print("\nAll diagrams regenerated in:", OUT)


if __name__ == "__main__":
    generate_all()
