# Question 1 

# Task 1


class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

# Demonstration script
vehicle1 = Vehicle("ABC123", "Car", "John Doe")
vehicle2 = Vehicle("XYZ789", "Truck", "Jane Smith")

print(f"Vehicle 1: {vehicle1.registration_number}, {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2: {vehicle2.registration_number}, {vehicle2.type}, Owner: {vehicle2.owner}")

# Update owners
vehicle1.update_owner("Alice Johnson")
vehicle2.update_owner("Bob Brown")

print("\nAfter updating owners:")
print(f"Vehicle 1: {vehicle1.registration_number}, {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2: {vehicle2.registration_number}, {vehicle2.type}, Owner: {vehicle2.owner}")