#5:: Use Linked List to track data dynamically in freight management system for logistics companies.
class Node:
    """Node to store a checkpoint."""
    def __init__(self, data):
        self.data = data  
        self.next = None  


class LinkedList:
    """Linked List to track shipment checkpoints."""
    def __init__(self):
        self.head = None  

    def add_checkpoint(self, data):
        """Add a checkpoint to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_checkpoint(self, data):
        """Remove a checkpoint by its data."""
        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next

    def display_checkpoints(self):
        """Display all checkpoints in the journey."""
        current = self.head
        checkpoints = []
        while current:
            checkpoints.append(current.data)
            current = current.next
        return checkpoints

shipment_tracking = LinkedList()


shipment_tracking.add_checkpoint("Warehouse A - Dispatched")
shipment_tracking.add_checkpoint("Checkpoint 1 - In Transit")
shipment_tracking.add_checkpoint("Checkpoint 2 - Arrived at Sorting Hub")
shipment_tracking.add_checkpoint("Checkpoint 3 - Kigali")
shipment_tracking.add_checkpoint("Checkpoint 4 - huye")
shipment_tracking.add_checkpoint("Destination - Delivered")


print("Shipment Checkpoints:")
print(shipment_tracking.display_checkpoints())


shipment_tracking.remove_checkpoint("Checkpoint 2 - Arrived at Sorting Hub")

print("\nUpdated Shipment Checkpoints:")
print(shipment_tracking.display_checkpoints())
