# 6: Implement a tree to represent hierarchical data in the freight management system for logistics companies.
class TreeNode:
    """Node to represent a single hub or checkpoint in the freight management system."""
    def __init__(self, name, data=None):
        self.name = name  
        self.data = data 
        self.children = []  

    def add_child(self, child_node):
        """Add a child to the current node."""
        self.children.append(child_node)

    def remove_child(self, child_name):
        """Remove a child by name."""
        self.children = [child for child in self.children if child.name != child_name]

    def display(self, level=0):
        """Recursively display the tree structure."""
        print("  " * level + f"- {self.name} ({self.data})")
        for child in self.children:
            child.display(level + 1)



main_hub = TreeNode("Main Distribution Hub", data={"capacity": 1000, "location": "City A"})


regional_hub_1 = TreeNode("Regional Hub 1", data={"capacity": 500, "location": "City B"})
regional_hub_2 = TreeNode("Regional Hub 2", data={"capacity": 700, "location": "City C"})


local_hub_1 = TreeNode("Local Hub 1", data={"capacity": 200, "location": "City D"})
local_hub_2 = TreeNode("Local Hub 2", data={"capacity": 300, "location": "City E"})
regional_hub_1.add_child(local_hub_1)
regional_hub_1.add_child(local_hub_2)


local_hub_3 = TreeNode("Local Hub 3", data={"capacity": 250, "location": "City F"})
local_hub_4 = TreeNode("Local Hub 4", data={"capacity": 450, "location": "City G"})
regional_hub_2.add_child(local_hub_3)
regional_hub_2.add_child(local_hub_4)


main_hub.add_child(regional_hub_1)
main_hub.add_child(regional_hub_2)


print("Shipping Hub Hierarchy:")
main_hub.display()


def find_node(root, name):
    """Find a node in the tree by its name."""
    if root.name == name:
        return root
    for child in root.children:
        result = find_node(child, name)
        if result:
            return result
    return None

search_result = find_node(main_hub, "Local Hub 3")
if search_result:
    print(f"\nFound: {search_result.name} ({search_result.data})")
else:
    print("\nHub not found.")


new_local_hub = TreeNode("New Local Hub", data={"capacity": 150, "location": "City H"})
regional_hub_2.add_child(new_local_hub)


regional_hub_1.remove_child("Local Hub 1")


print("\nUpdated Shipping Hub Hierarchy:")
main_hub.display()
