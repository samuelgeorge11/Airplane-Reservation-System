from data import flights

def add_flight():
    flight_number = input("Enter a new flight number: ")
    flight_details = {
        "source": input("Enter the departure location: "),
        "destination": input("Enter the destination: "),
        "seats": int(input("Enter the number of seats available: ")),
        "booked_seats": 0,
        "date": input("Enter the flight date (YYYY-MM-DD): "),
        "price": float(input("Enter the ticket price: "))
    }
    flights[flight_number] = flight_details
    print(f"Flight {flight_number} added successfully!\n")

def display_flights():
    print("Current Flights:")
    for flight_num, details in flights.items():
        available_seats = details["seats"] - details["booked_seats"]
        print(
            f"Flight {flight_num}: {details['source']} -> {details['destination']}, "
            f"Date: {details['date']}, Available Seats: {available_seats}, "
            f"Price: ${details['price']:.2f}"
        )
    print()
