#2: Implement Array and Queue to manage data in the freight management system for logistics companies.
class Shipment:
    def __init__(self, shipment_id, origin, destination, weight, status="Pending"):
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.status = status
        self.carrier = None

    def update_status(self, status):
        self.status = status
        print(f"Shipment {self.shipment_id} status updated to {status}")

    def assign_carrier(self, carrier):
        self.carrier = carrier
        print(f"Carrier '{carrier.name}' assigned to shipment {self.shipment_id}")

class Carrier:
    def __init__(self, carrier_id, name, max_weight_capacity):
        self.carrier_id = carrier_id
        self.name = name
        self.max_weight_capacity = max_weight_capacity

    def add_shipment(self, shipment):
        if shipment.weight <= self.max_weight_capacity:
            shipment.assign_carrier(self)
            print(f"Shipment {shipment.shipment_id} added to carrier {self.name}")
        else:
            print(f"Carrier {self.name} cannot carry shipment {shipment.shipment_id}, exceeds weight capacity")

    def __str__(self):
        return f"Carrier {self.name}, Max Capacity: {self.max_weight_capacity}"

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Shipment {item.shipment_id} added to queue.")

    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Shipment {item.shipment_id} processed.")
            return item
        else:
            print("Queue is empty.")
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def display_queue(self):
        if not self.is_empty():
            print("Shipments in Queue:")
            for item in self.queue:
                print(f"- Shipment ID: {item.shipment_id}, Status: {item.status}")
        else:
            print("Queue is empty.")

class FreightManagementSystem:
    def __init__(self):
        self.shipments = []
        self.carriers = []
        self.order_queue = Queue()

    def add_shipment(self, shipment):
        self.shipments.append(shipment)
        print(f"Shipment {shipment.shipment_id} added to the system.")

    def add_carrier(self, carrier):
        self.carriers.append(carrier)
        print(f"Carrier {carrier.name} added to the system.")

    def get_shipment(self, shipment_id):
        for shipment in self.shipments:
            if shipment.shipment_id == shipment_id:
                return shipment
        print(f"Shipment {shipment_id} not found.")
        return None

    def get_carrier(self, carrier_id):
        for carrier in self.carriers:
            if carrier.carrier_id == carrier_id:
                return carrier
        print(f"Carrier {carrier_id} not found.")
        return None

    def assign_carrier_to_shipment(self, shipment_id, carrier_id):
        shipment = self.get_shipment(shipment_id)
        carrier = self.get_carrier(carrier_id)

        if shipment and carrier:
            carrier.add_shipment(shipment)

    def track_shipment(self, shipment_id):
        shipment = self.get_shipment(shipment_id)
        if shipment:
            print(f"Shipment {shipment.shipment_id}: {shipment.status}")
        else:
            print(f"Shipment {shipment_id} not found.")

    def process_orders(self):
        while not self.order_queue.is_empty():
            shipment = self.order_queue.dequeue()
            print(f"Processing shipment {shipment.shipment_id}.")
            shipment.update_status("In Transit")

    def add_shipment_to_queue(self, shipment_id):
        shipment = self.get_shipment(shipment_id)
        if shipment:
            self.order_queue.enqueue(shipment)

    def display_all_shipments(self):
        print("All Shipments:")
        for shipment in self.shipments:
            print(f"- Shipment ID: {shipment.shipment_id}, Status: {shipment.status}")

def main():
    system = FreightManagementSystem()

    carrier1 = Carrier(1, "Logistics Express", 1000)
    carrier2 = Carrier(2, "Fast Track Transport", 500)

    system.add_carrier(carrier1)
    system.add_carrier(carrier2)

    shipment1 = Shipment(101, "New York", "Los Angeles", 400)
    shipment2 = Shipment(102, "Chicago", "San Francisco", 1200)

    system.add_shipment(shipment1)
    system.add_shipment(shipment2)

    system.add_shipment_to_queue(101)
    system.add_shipment_to_queue(102)

    system.assign_carrier_to_shipment(101, 1)
    system.assign_carrier_to_shipment(102, 2)

    system.display_all_shipments()
    system.order_queue.display_queue()

    system.process_orders()

if __name__ == "__main__":
    main()
