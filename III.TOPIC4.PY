#4: Create Binary Search Tree (BST) to manage a fixed number of orders in the freight management system for logistics companies.
class Order:
    def __init__(self, order_id, origin, destination, weight, status="Pending"):
        self.order_id = order_id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.status = status

    def __str__(self):
        return f"Order ID: {self.order_id}, Origin: {self.origin}, Destination: {self.destination}, Weight: {self.weight}, Status: {self.status}"

class Node:
    def __init__(self, order):
        self.order = order
        self.left = None
        self.right = None

class BST:
    def __init__(self, max_orders):
        self.root = None
        self.max_orders = max_orders
        self.current_orders = 0

    def insert(self, order):
        if self.current_orders >= self.max_orders:
            print("Order limit reached! Cannot insert more orders.")
            return
        
        self.root = self._insert(self.root, order)
        self.current_orders += 1
        print(f"Order {order.order_id} inserted.")

    def _insert(self, root, order):
        if root is None:
            return Node(order)

        if order.order_id < root.order.order_id:
            root.left = self._insert(root.left, order)
        elif order.order_id > root.order.order_id:
            root.right = self._insert(root.right, order)

        return root

    def search(self, order_id):
        result = self._search(self.root, order_id)
        if result:
            print(f"Order found: {result.order}")
        else:
            print(f"Order ID {order_id} not found.")

    def _search(self, root, order_id):
        if root is None or root.order.order_id == order_id:
            return root

        if order_id < root.order.order_id:
            return self._search(root.left, order_id)

        return self._search(root.right, order_id)

    def delete(self, order_id):
        self.root = self._delete(self.root, order_id)

    def _delete(self, root, order_id):
        if root is None:
            print(f"Order ID {order_id} not found.")
            return root

        if order_id < root.order.order_id:
            root.left = self._delete(root.left, order_id)
        elif order_id > root.order.order_id:
            root.right = self._delete(root.right, order_id)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self._min_value_node(root.right)
            root.order = temp.order
            root.right = self._delete(root.right, temp.order.order_id)

        return root

    def _min_value_node(self, root):
        while root.left is not None:
            root = root.left
        return root

    def inorder_traversal(self):
        print("Orders in the system:")
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, root):
        if root:
            self._inorder_traversal(root.left)
            print(root.order)
            self._inorder_traversal(root.right)

class FreightManagementSystem:
    def __init__(self, max_orders):
        self.bst = BST(max_orders)

    def add_order(self, order):
        self.bst.insert(order)

    def search_order(self, order_id):
        self.bst.search(order_id)

    def remove_order(self, order_id):
        self.bst.delete(order_id)

    def display_orders(self):
        self.bst.inorder_traversal()

def main():
    system = FreightManagementSystem(max_orders=5)

    order1 = Order(101, "KIGALI", "GASABO", 3100)
    order2 = Order(102, "RUSIZI", "KAMEMBE", 3300)
    order3 = Order(103, "HUYE", "TUMBA", 8900)
    order4 = Order(104, "MUSANZE", "MUSANZE CITY BRAZER", 800)
    order5 = Order(105, "HUYE", "NGOMA", 700)

    system.add_order(order1)
    system.add_order(order2)
    system.add_order(order3)
    system.add_order(order4)
    system.add_order(order5)

    system.display_orders()

    system.search_order(102)

    system.remove_order(102)

    system.display_orders()

    system.add_order(Order(106, "Dallas", "Phoenix", 200))  # Will fail as order limit is reached

if __name__ == "__main__":
    main()
