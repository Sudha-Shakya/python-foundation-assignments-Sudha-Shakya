# Question 4: Shared Booking Counter (Scope & the `global` keyword)


total_seats_booked = 0

def book_seats(n):
    global total_seats_booked

    total_seats_booked = total_seats_booked+n

    print(f"booked{n} seats(s). Total booked so far:{total_seats_booked}")

    
def reset_bookings():
    global total_seats_booked
    
    total_seats_booked=0
  
# --- test your functions below ---
book_seats(3)
book_seats(5)
reset_bookings()
book_seats(2)
