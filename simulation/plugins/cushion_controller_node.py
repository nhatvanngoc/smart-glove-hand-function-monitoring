"""
ROS2 Cushion Controller Node
=============================
ROS2 node that subscribes to /cushion/cmd (PID setpoints from Jetson)
and publishes /cushion/pressure (simulated pressure from dynamics).

Compatible with both Gazebo (via plugin) and standalone test.

Standalone usage:
    python3 cushion_controller_node.py --standalone --duration 60
"""
from __future__ import annotations
import sys, os
import argparse
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))


def run_standalone(duration_s: float = 60.0, max_p: float = 80.0):
    """Run cushion controller without ROS2 (for testing)."""
    from simulation.plugins.cushion_dynamics_simulator import CushionDynamics

    cushion = CushionDynamics(max_p=max_p, tau=0.3, dt=0.1)
    sacrum_zone = (slice(3, 6), slice(3, 6))
    print(f"\n[Standalone] Cushion controller running for {duration_s:.0f}s...")

    t = 0.0
    while t < duration_s:
        current_p = cushion.get_pressure()
        high = current_p > 50
        cmd = np.full((8, 8), 28.0, dtype=np.float32)
        cmd[sacrum_zone] = 15.0
        cmd[high] = 10.0
        cmd[7, :] = 18.0

        if t > 5.0:
            cushion.add_disturbance(sacrum_pressure=30.0)
        cushion.step(cmd)
        if int(t) % 5 == 0:
            print(f"t={t:5.1f}s | peak={cushion.p.max():.1f} | "
                  f"sacrum={cushion.p[sacrum_zone].mean():.1f} | "
                  f"safe={cushion.p.max() < 80}")
        t += cushion.dt

    print("\n[Standalone] Simulation complete.")
    return cushion.get_pressure()


def run_ros2_node():
    """Run as ROS2 node (requires rclpy)."""
    try:
        import rclpy
        from rclpy.node import Node
        from std_msgs.msg import Float32MultiArray, Bool
    except ImportError:
        print("[ROS2] rclpy not available - run with --standalone flag")
        return

    from simulation.plugins.cushion_dynamics_simulator import CushionDynamics

    class CushionControllerNode(Node):
        def __init__(self):
            super().__init__("cushion_controller")
            self.cushion = CushionDynamics(max_p=80.0, tau=0.3, dt=0.1)
            self.sub_cmd = self.create_subscription(
                Float32MultiArray, "/cushion/cmd", self.cb_cmd, 10)
            self.pub_pressure = self.create_publisher(
                Float32MultiArray, "/cushion/pressure", 10)
            self.pub_safety = self.create_publisher(
                Bool, "/system/safety", 10)
            self.timer = self.create_timer(0.1, self.tick)
            self.get_logger().info("CushionController started @ 10 Hz")

        def cb_cmd(self, msg):
            if len(msg.data) == 64:
                sp = np.array(msg.data, dtype=np.float32).reshape(8, 8)
                self.cushion.cmd = sp

        def tick(self):
            self.cushion.step(self.cushion.cmd)
            self.cushion.add_disturbance(sacrum_pressure=30.0)
            msg_p = Float32MultiArray()
            msg_p.data = self.cushion.get_pressure().flatten().tolist()
            self.pub_pressure.publish(msg_p)
            safe = bool(self.cushion.p.max() < 80.0)
            self.pub_safety.publish(Bool(data=safe))

    rclpy.init()
    node = CushionControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--standalone", action="store_true")
    parser.add_argument("--duration", type=float, default=60.0)
    args = parser.parse_args()

    if args.standalone:
        run_standalone(duration_s=args.duration)
    else:
        run_ros2_node()
