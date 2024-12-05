import rclpy
from rclpy.node import Node
import random


class BehaviorTreeNode(Node):
    def __init__(self):
        super().__init__('behavior_tree_node')
        self.get_logger().info("Behavior Tree Node initialized.")
        self.run_behavior_tree()

    def run_behavior_tree(self):
        # Define the behavior tree
        while True:
            if self.execute_sequence():
                self.get_logger().info("Behavior Tree Execution Successful! Node shutting down.")
                rclpy.shutdown()  # Shutdown the ROS 2 system
                break  # Exit the loop
            else:
                self.get_logger().warn("Behavior Tree Execution Failed. Retrying...")

    def execute_sequence(self):
        if not self.user_input_action("Check Environment"):
            return False
        if not self.user_input_action("Approach Target"):
            return False
        if not self.user_input_action("Perform Task"):
            return False
        return True

    def user_input_action(self, action_name):
        random_number = random.randint(0, 9)
        self.get_logger().info(f"[{action_name}] Random number generated: {random_number}")
        user_input = input(f"Enter the number for [{action_name}] to proceed: ")
        try:
            user_input = int(user_input)
        except ValueError:
            self.get_logger().error(f"Invalid input. Expected a number between 0 and 9.")
            return False
        if user_input == random_number:
            self.get_logger().info(f"[{action_name}] Success!")
            return True
        else:
            self.get_logger().warn(f"[{action_name}] Failed. Input: {user_input}, Expected: {random_number}")
            return False


def main(args=None):
    rclpy.init(args=args)
    node = BehaviorTreeNode()
    node.destroy_node()
