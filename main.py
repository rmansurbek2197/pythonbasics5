class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
        self.bookings = []

class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.is_booked = False

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Booking:
    def __init__(self, customer, room, date):
        self.customer = customer
        self.room = room
        self.date = date

class HotelBookingSystem:
    def __init__(self, hotel):
        self.hotel = hotel

    def book_room(self, customer, room_number, date):
        for room in self.hotel.rooms:
            if room.number == room_number and not room.is_booked:
                room.is_booked = True
                booking = Booking(customer, room, date)
                self.hotel.bookings.append(booking)
                return booking
        return None

    def cancel_booking(self, booking):
        for b in self.hotel.bookings:
            if b == booking:
                self.hotel.bookings.remove(b)
                b.room.is_booked = False
                return True
        return False

    def get_bookings(self):
        return self.hotel.bookings

hotel = Hotel("My Hotel", [Room(1, 2), Room(2, 3), Room(3, 1)])
system = HotelBookingSystem(hotel)

customer1 = Customer("John Doe", "john@example.com")
customer2 = Customer("Jane Doe", "jane@example.com")

booking1 = system.book_room(customer1, 1, "2024-09-16")
booking2 = system.book_room(customer2, 2, "2024-09-17")

print(booking1.customer.name)
print(booking1.room.number)
print(booking1.date)

system.cancel_booking(booking1)

bookings = system.get_bookings()
for booking in bookings:
    print(booking.customer.name)
    print(booking.room.number)
    print(booking.date)

class Payment:
    def __init__(self, booking, amount):
        self.booking = booking
        self.amount = amount

class PaymentSystem:
    def __init__(self):
        self.payments = []

    def make_payment(self, booking, amount):
        payment = Payment(booking, amount)
        self.payments.append(payment)
        return payment

payment_system = PaymentSystem()
payment1 = payment_system.make_payment(booking2, 100)
payment2 = payment_system.make_payment(booking2, 50)

for payment in payment_system.payments:
    print(payment.booking.customer.name)
    print(payment.booking.room.number)
    print(payment.amount)

class Invoice:
    def __init__(self, payment):
        self.payment = payment

    def generate_invoice(self):
        return f"Invoice for {self.payment.booking.customer.name} - Room {self.payment.booking.room.number} - {self.payment.amount}"

invoice1 = Invoice(payment1)
print(invoice1.generate_invoice())
invoice2 = Invoice(payment2)
print(invoice2.generate_invoice())