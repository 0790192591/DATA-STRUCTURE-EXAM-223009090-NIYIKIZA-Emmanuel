#3: Implement AVL Tree for freight management system for logistics companies processing.
class Shipment:
    def __init__(self, shipment_id, origin, destination, weight, status="Pending"):
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.status = status
        self.carrier = None

    def __str__(self):
        return f"Shipment ID: {self.shipment_id}, Origin: {self.origin}, Destination: {self.destination}, Weight: {self.weight}, Status: {self.status}"

class Node:
    def __init__(self, shipment):
        self.shipment = shipment
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, shipment):
        if not root:
            return Node(shipment)

        if shipment.shipment_id < root.shipment.shipment_id:
            root.left = self.insert(root.left, shipment)
        else:
            root.right = self.insert(root.right, shipment)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

     
        if balance > 1 and shipment.shipment_id < root.left.shipment.shipment_id:
            return self.right_rotate(root)

      
        if balance < -1 and shipment.shipment_id > root.right.shipment.shipment_id:
            return self.left_rotate(root)

      
        if balance > 1 and shipment.shipment_id > root.left.shipment.shipment_id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        
        if balance < -1 and shipment.shipment_id < root.right.shipment.shipment_id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def pre_order_traversal(self, root):
        if not root:
            return
        print(root.shipment)
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

    def search(self, root, shipment_id):
        if not root or root.shipment.shipment_id == shipment_id:
            return root

        if shipment_id < root.shipment.shipment_id:
            return self.search(root.left, shipment_id)

        return self.search(root.right, shipment_id)

    def delete(self, root, shipment_id):
        if not root:
            return root

        if shipment_id < root.shipment.shipment_id:
            root.left = self.delete(root.left, shipment_id)
        elif shipment_id > root.shipment.shipment_id:
            root.right = self.delete(root.right, shipment_id)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            min_node = self.get_min_node(root.right)
            root.shipment = min_node.shipment
            root.right = self.delete(root.right, min_node.shipment.shipment_id)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_min_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

class FreightManagementSystem:
    def __init__(self):
        self.avl_tree = AVLTree()

    def add_shipment(self, shipment):
        self.avl_tree.root = self.avl_tree.insert(self.avl_tree.root, shipment)
        print(f"Shipment {shipment.shipment_id} added to the system.")

    def remove_shipment(self, shipment_id):
        self.avl_tree.root = self.avl_tree.delete(self.avl_tree.root, shipment_id)
        print(f"Shipment {shipment_id} removed from the system.")

    def search_shipment(self, shipment_id):
        result = self.avl_tree.search(self.avl_tree.root, shipment_id)
        if result:
            print(f"Shipment found: {result.shipment}")
        else:
            print(f"Shipment {shipment_id} not found.")

    def display_all_shipments(self):
        print("Shipments in the system:")
        self.avl_tree.pre_order_traversal(self.avl_tree.root)

def main():
    system = FreightManagementSystem()

    shipment1 = Shipment(101, "KIGALI", "GASABO", 546)
    shipment2 = Shipment(102, "HUYE", "TUMBA", 4500)
    shipment3 = Shipment(103, "RUSIZI", "KAMEMBE", 100)

    system.add_shipment(shipment1)
    system.add_shipment(shipment2)
    system.add_shipment(shipment3)

    system.display_all_shipments()

    system.search_shipment(102)
    system.remove_shipment(102)
    system.display_all_shipments()

if __name__ == "__main__":
    main()
