from data import flights

def search_flights():
    source = input("Enter departure location: ").lower()
    destination = input("Enter destination location: ").lower()
    date = input("Enter preferred date (YYYY-MM-DD, or press Enter to skip): ")

    print(f"Flights from {source.capitalize()} to {destination.capitalize()}:")
    found_flights = False

    for flight_num, details in flights.items():
        if (
            details["source"].lower() == source
            and details["destination"].lower() == destination
            and (not date or details["date"] == date)
        ):
            available_seats = details["seats"] - details["booked_seats"]
            print(
                f"Flight {flight_num}: Date: {details['date']}, "
                f"Available Seats: {available_seats}, Price: ${details['price']:.2f}"
            )
            found_flights = True

    if not found_flights:
        print("No flights found for this route and date.\n")
