import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool
import py_trees
import time


class MoveCobotNode(py_trees.behaviour.Behaviour):
    def __init__(self, node, angles):
        super().__init__(name="MoveCobotNode")
        self.node = node
        self.angles = angles
        self.publisher = node.create_publisher(String, 'cobot_move_command', 10)
        self.subscription = node.create_subscription(Bool, 'cobot_move_feedback', self.feedback_callback, 10)
        self.feedback_received = False
        self.success = False

    def feedback_callback(self, msg):
        """코봇의 피드백을 처리."""
        self.node.get_logger().info(f"Feedback received from cobot: {msg.data}")
        self.feedback_received = True
        self.success = msg.data

    def initialise(self):
        """초기화 및 코봇 이동 명령 전송."""
        self.node.get_logger().info(f"Initializing movement to angles: {self.angles}")
        angles_str = ",".join(map(str, self.angles))
        self.publisher.publish(String(data=angles_str))
        self.feedback_received = False

    def update(self):
        """코봇 상태 업데이트."""
        if not self.feedback_received:
            self.node.get_logger().info("Waiting for cobot to complete movement...")
            return py_trees.common.Status.RUNNING
        else:
            if self.success:
                self.node.get_logger().info("Cobot movement completed successfully.")
                return py_trees.common.Status.SUCCESS
            else:
                self.node.get_logger().error("Cobot movement failed.")
                return py_trees.common.Status.FAILURE


class MoveAGVNode(py_trees.behaviour.Behaviour):
    def __init__(self, node):
        super().__init__(name="MoveAGVNode")
        self.node = node
        self.publisher = node.create_publisher(String, 'agv_move_command', 10)
        self.subscription = node.create_subscription(Bool, 'agv_move_feedback', self.feedback_callback, 10)
        self.feedback_received = False
        self.success = False

    def feedback_callback(self, msg):
        """AGV의 피드백을 처리."""
        self.node.get_logger().info(f"Feedback received from AGV: {msg.data}")
        self.feedback_received = True
        self.success = msg.data

    def initialise(self):
        """초기화 및 AGV 이동 명령 전송."""
        self.node.get_logger().info("Initializing AGV movement...")
        self.publisher.publish(String(data="move"))
        self.feedback_received = False

    def update(self):
        """AGV 상태 업데이트."""
        if not self.feedback_received:
            self.node.get_logger().info("Waiting for AGV to complete movement...")
            return py_trees.common.Status.RUNNING
        else:
            if self.success:
                self.node.get_logger().info("AGV movement completed successfully.")
                return py_trees.common.Status.SUCCESS
            else:
                self.node.get_logger().error("AGV movement failed.")
                return py_trees.common.Status.FAILURE


class DelayNode(py_trees.behaviour.Behaviour):
    def __init__(self, node, delay_time):
        super().__init__(name="DelayNode")
        self.node = node
        self.delay_time = delay_time
        self.start_time = None

    def initialise(self):
        """지연 타이머 초기화."""
        self.start_time = time.time()
        self.node.get_logger().info(f"Delay started for {self.delay_time} seconds.")

    def update(self):
        """지연 상태 업데이트."""
        elapsed_time = time.time() - self.start_time
        if elapsed_time < self.delay_time:
            return py_trees.common.Status.RUNNING
        else:
            self.node.get_logger().info(f"Delay completed ({self.delay_time} seconds).")
            return py_trees.common.Status.SUCCESS


class BehaviorTreeExecutor(Node):
    def __init__(self):
        super().__init__('bt_executor')

        # Define joint angles
        initial_angles = [45, -30, 90, -45, 60, 0]
        return_angles = [0, 0, 0, 0, 0, 0]

        # Build the behavior tree
        root = py_trees.composites.Sequence(name="Root Sequence", memory=True)

        # Add cobot movement to initial position
        move_cobot_to_initial = MoveCobotNode(self, initial_angles)

        # Add delay after cobot movement
        delay_after_cobot = DelayNode(self, delay_time=3.0)

        # Add AGV movement
        move_agv_node = MoveAGVNode(self)

        # Add cobot movement to return position
        move_cobot_to_return = MoveCobotNode(self, return_angles)

        # Add delay after cobot returns
        delay_after_cobot_return = DelayNode(self, delay_time=3.0)

        # Add second AGV movement
        move_agv_node_second = MoveAGVNode(self)

        # Add nodes to the sequence
        root.add_children([
            move_cobot_to_initial,
            delay_after_cobot,
            move_agv_node,
            move_cobot_to_return,
            delay_after_cobot_return,
            move_agv_node_second
        ])

        # Create the behavior tree
        self.behaviour_tree = py_trees.trees.BehaviourTree(root)

        self.get_logger().info("Behavior Tree Executor initialized.")

    def execute_tree(self):
        """Behavior Tree 실행."""
        self.get_logger().info("Starting Behavior Tree execution...")
        while rclpy.ok():
            result = self.behaviour_tree.tick()
            if result == py_trees.common.Status.SUCCESS:
                self.get_logger().info("Behavior Tree execution completed successfully.")
                break
            elif result == py_trees.common.Status.FAILURE:
                self.get_logger().error("Behavior Tree execution failed.")
                break
            rclpy.spin_once(self, timeout_sec=0.1)


def main(args=None):
    rclpy.init(args=args)
    executor = BehaviorTreeExecutor()
    executor.execute_tree()
    executor.destroy_node()
    rclpy.shutdown()
