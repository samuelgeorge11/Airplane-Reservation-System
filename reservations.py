import datetime
from data import flights, reservations
from flights import display_flights

def book_flight():
    display_flights()
    flight_number = input("Enter the flight number to book: ")

    if flight_number not in flights:
        print("Flight not found.\n")
        return

    flight = flights[flight_number]
    if flight["booked_seats"] >= flight["seats"]:
        print("Sorry, no seats available.\n")
        return

    passenger_name = input("Enter the passenger's name: ")
    passenger_email = input("Enter the passenger's email: ")

    flight["booked_seats"] += 1
    reservation_id = f"{flight_number}-{flight['booked_seats']}"

    reservations[reservation_id] = {
        "flight_number": flight_number,
        "passenger_name": passenger_name,
        "passenger_email": passenger_email,
        "booking_date": datetime.date.today().isoformat()
    }

    print(f"Booking successful! Reservation ID: {reservation_id}")
    print(f"Total price: ${flight['price']:.2f}\n")

def cancel_reservation():
    reservation_id = input("Enter your reservation ID to cancel: ")

    if reservation_id not in reservations:
        print("Reservation ID not found.\n")
        return

    flight_number = reservations[reservation_id]["flight_number"]
    flights[flight_number]["booked_seats"] -= 1
    del reservations[reservation_id]

    print(f"Reservation {reservation_id} canceled successfully.\n")

def display_reservations():
    print("All Reservations:")

    for flight_number, flight_details in flights.items():
        print(
            f"\nFlight {flight_number} "
            f"({flight_details['source']} -> {flight_details['destination']}):"
        )

        passengers = [
            (res["passenger_name"], res["passenger_email"])
            for res in reservations.values()
            if res["flight_number"] == flight_number
        ]

        if passengers:
            for name, email in passengers:
                print(f"- {name} ({email})")
        else:
            print("No reservations for this flight.")

    print()
