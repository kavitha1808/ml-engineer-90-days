# Seat Booking System — Real-World Logic

This module implements a simple seat booking system similar to
train, bus, or movie ticket platforms.

---

## Seat Representation

- 0 → Available
- 1 → Booked

Seats are stored in a list to simulate database-like behavior.

---

## Supported Operations

- Display seat availability
- Book a seat
- Cancel a booking
- Prevent duplicate bookings
- Count available seats

---

## Engineering Insight

User inputs are 1-based, while Python indexing is 0-based.
The system correctly handles this mapping — a common real-world bug source.
