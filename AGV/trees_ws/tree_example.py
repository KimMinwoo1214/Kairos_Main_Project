import random
from abc import ABC, abstractmethod


class Node(ABC):
    """Abstract base class for all behavior tree nodes."""
    @abstractmethod
    def run(self):
        pass


class Selector(Node):
    """Selector node: Runs children until one succeeds."""
    def __init__(self, children):
        self.children = children

    def run(self):
        for child in self.children:
            if child.run():
                return True
        return False


class Sequence(Node):
    """Sequence node: Runs children until one fails."""
    def __init__(self, children):
        self.children = children

    def run(self):
        for child in self.children:
            if not child.run():
                return False
        return True


class Action(Node):
    """Action node: Executes an action."""
    def __init__(self, action_fn, description):
        self.action_fn = action_fn
        self.description = description

    def run(self):
        print(f"Executing node: {self.description}")
        return self.action_fn()


# Helper function to simulate random number generation and user input
def user_input_action(node_name):
    random_number = random.randint(0, 9)  # Random number between 0 and 9
    print(f"[{node_name}] Random number generated: {random_number}")
    user_input = int(input(f"Enter the number for [{node_name}] to proceed: "))
    if user_input == random_number:
        print(f"[{node_name}] Success!")
        return True
    else:
        print(f"[{node_name}] Failed. Input: {user_input}, Expected: {random_number}")
        return False


# Example nodes
def check_environment():
    return user_input_action("Check Environment")

def approach_target():
    return user_input_action("Approach Target")

def perform_task():
    return user_input_action("Perform Task")


# Constructing the behavior tree
if __name__ == "__main__":
    # Leaf actions
    check_node = Action(check_environment, "Check if environment is safe")
    approach_node = Action(approach_target, "Approach the target")
    task_node = Action(perform_task, "Perform the main task")

    # Higher level structure
    task_sequence = Sequence([check_node, approach_node, task_node])
    root_selector = Selector([task_sequence])

    # Run the behavior tree
    print("Behavior Tree Execution:")
    while not root_selector.run():
        print("Retrying Behavior Tree...")
