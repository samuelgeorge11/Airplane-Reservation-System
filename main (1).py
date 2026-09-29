import os

from flights import add_flight, display_flights
from reservations import (
    book_flight,
    cancel_reservation,
    display_reservations
)
from search import search_flights
from reports import generate_report

def main():
    menu_options = {
        "1": ("Add Flight", add_flight),
        "2": ("Book Flight", book_flight),
        "3": ("Cancel Reservation", cancel_reservation),
        "4": ("Display Flights", display_flights),
        "5": ("Display All Reservations", display_reservations),
        "6": ("Search Flights", search_flights),
        "7": ("Generate Report", generate_report),
        "8": ("Exit", None)
    }

    while True:
        print("Airline Reservation System")
        for key, (option, _) in menu_options.items():
            print(f"{key}. {option}")

        choice = input("Choose an option (1-8): ")

        if choice == "8":
            print("Thank you for using the Airline Reservation System!")
            break
        elif choice in menu_options:
            menu_options[choice][1]()
            input("\nPress Enter to continue...")
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print("Invalid choice. Please try again.\n")
            input("\nPress Enter to continue...")
            os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()
