from data import flights

def generate_report():
    total_bookings = sum(
        flight["booked_seats"] for flight in flights.values()
    )
    total_revenue = sum(
        flight["booked_seats"] * flight["price"]
        for flight in flights.values()
    )

    print("Flight Report:")

    for flight_num, details in flights.items():
        bookings = details["booked_seats"]
        revenue = bookings * details["price"]
        print(
            f"Flight {flight_num}: Bookings: {bookings}, "
            f"Revenue: ${revenue:.2f}"
        )

    print(f"\nTotal Bookings: {total_bookings}")
    print(f"Total Revenue: ${total_revenue:.2f}\n")
