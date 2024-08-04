# Question 1 

# Task 1


class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

# User input for creating Vehicle instances
reg_num1 = input("Enter registration number for Vehicle 1: ")
type1 = input("Enter type for Vehicle 1: ")
owner1 = input("Enter owner for Vehicle 1: ")

reg_num2 = input("Enter registration number for Vehicle 2: ")
type2 = input("Enter type for Vehicle 2: ")
owner2 = input("Enter owner for Vehicle 2: ")

vehicle1 = Vehicle(reg_num1, type1, owner1)
vehicle2 = Vehicle(reg_num2, type2, owner2)

print(f"\nVehicle 1: {vehicle1.registration_number}, {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2: {vehicle2.registration_number}, {vehicle2.type}, Owner: {vehicle2.owner}")

# User input for updating owners
new_owner1 = input("\nEnter new owner for Vehicle 1: ")
new_owner2 = input("Enter new owner for Vehicle 2: ")

vehicle1.update_owner(new_owner1)
vehicle2.update_owner(new_owner2)

print("\nAfter updating owners:")
print(f"Vehicle 1: {vehicle1.registration_number}, {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2: {vehicle2.registration_number}, {vehicle2.type}, Owner: {vehicle2.owner}")


# Task 2


class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
        return self.participant_count

# User input for creating an Event instance
event_name = input("Enter the event name: ")
event_date = input("Enter the event date (YYYY-MM-DD): ")

event = Event(event_name, event_date)

print(f"\nEvent: {event.name}, Date: {event.date}, Participants: {event.get_participant_count()}")

# User input for adding participants
num_participants = int(input("\nEnter the number of participants to add: "))
for _ in range(num_participants):
    event.add_participant()

print(f"After adding participants: {event.get_participant_count()}")