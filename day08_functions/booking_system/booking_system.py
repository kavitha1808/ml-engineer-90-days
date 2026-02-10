seats = [0, 0, 0, 0, 0]

def show_seats():
    for i in range(len(seats)):
        status = "Booked" if seats[i] == 1 else "Available"
        print(f"Seat {i+1}: {status}")

def book_seat(seat_no):
    if seat_no < 1 or seat_no > len(seats):
        print("Invalid seat number")
        return

    if seats[seat_no - 1] == 1:
        print("Seat already booked")
    else:
        seats[seat_no - 1] = 1
        print("Seat booked")

def cancel_seat(seat_no):
    if seats[seat_no - 1] == 0:
        print("Seat not booked")
    else:
        seats[seat_no - 1] = 0
        print("Booking cancelled")

def count_available_seats():
    count = 0
    for seat in seats:
        if seat == 0:
            count += 1
    return count

show_seats()
book_seat(2)
book_seat(2)
cancel_seat(2)
show_seats()
print("Available seats:", count_available_seats())
