#7: Use Bubble Sort to sort the freight management system for logistics companies data based on priority.
class Shipment:
    """Represents a shipment order with priority."""
    def __init__(self, order_id, destination, priority):
        self.order_id = order_id  
        self.destination = destination  
        self.priority = priority  

    def __str__(self):
        """String representation of the shipment."""
        return f"Order ID: {self.order_id}, Destination: {self.destination}, Priority: {self.priority}"

def bubble_sort(shipments):
    """Sorts a list of shipments based on priority using Bubble Sort."""
    
  
    priority_order = {'high': 1, 'medium': 2, 'low': 3}
    
    
    n = len(shipments)
    
    for i in range(n):
 
        swapped = False
        
        for j in range(0, n - i - 1):
            
            if priority_order[shipments[j].priority] > priority_order[shipments[j + 1].priority]:
               
                shipments[j], shipments[j + 1] = shipments[j + 1], shipments[j]
                swapped = True
        
       
        if not swapped:
            break

shipments = [
    Shipment(1, "KIGALI", "medium"),
    Shipment(2, "HUYE", "high"),
    Shipment(3, "RUSIZI", "low"),
    Shipment(4, "KARONGI", "high"),
    Shipment(5, "GICUMBI", "medium")
]


print("Original Shipment List:")
for shipment in shipments:
    print(shipment)


bubble_sort(shipments)


print("\nSorted Shipment List (by Priority):")
for shipment in shipments:
    print(shipment)
