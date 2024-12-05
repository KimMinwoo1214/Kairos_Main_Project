import py_trees_ros
import py_trees

def create_tree():
    root = py_trees.composites.Sequence("Root", memory = True)
    action = py_trees.behaviours.Dummy("Dummy Action")
    root.add_child(action)
    return root

def main():
    tree = create_tree()
    print("Behavior Tree created:", tree)

if __name__ == "__main__":
    tree = create_tree()
    print("Behavior Tree created:", tree)
