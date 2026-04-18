class Room:
    def __init__(self, number, capacity, price):
        self.number = number
        self.capacity = capacity
        self.price = price
        self.is_booked = False

class Booking:
    def __init__(self, customer, room, check_in, check_out):
        self.customer = customer
        self.room = room
        self.check_in = check_in
        self.check_out = check_out

class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.bookings = []

    def add_room(self, room):
        self.rooms.append(room)

    def book_room(self, customer, room, check_in, check_out):
        if not room.is_booked:
            booking = Booking(customer, room, check_in, check_out)
            self.bookings.append(booking)
            room.is_booked = True
            return True
        return False

    def cancel_booking(self, booking):
        if booking in self.bookings:
            self.bookings.remove(booking)
            booking.room.is_booked = False
            return True
        return False

hotel = Hotel("Grand Hotel")
room1 = Room(1, 2, 100)
room2 = Room(2, 3, 150)
hotel.add_room(room1)
hotel.add_room(room2)

customer1 = Customer("John Doe", "john@example.com", "1234567890")
customer2 = Customer("Jane Doe", "jane@example.com", "9876543210")

hotel.book_room(customer1, room1, "2024-01-01", "2024-01-03")
hotel.book_room(customer2, room2, "2024-01-05", "2024-01-08")

for booking in hotel.bookings:
    print(booking.customer.name, booking.room.number, booking.check_in, booking.check_out)