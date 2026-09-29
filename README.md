# Airline Reservation System (CLI)

A simple, command-line-based Airline Reservation System written in Python. This application allows users to manage flight schedules, book tickets, cancel reservations, and generate basic revenue reports using in-memory data storage.

## Features

*   **Add Flights:** Input new flights with details such as source, destination, seating capacity, date, and price.
*   **Book Flights:** Search for available flights and book tickets by providing passenger details. Automatically generates a unique reservation ID.
*   **Cancel Reservations:** Cancel existing bookings using the reservation ID. Automatically frees up the seat on the flight.
*   **Display Flights:** View a list of all current flights, including available seats and ticket prices.
*   **Display Reservations:** View a list of all passengers booked on each flight.
*   **Search Flights:** Find flights by specifying the departure location, destination, and an optional date.
*   **Generate Reports:** View total bookings and calculated revenue for each flight, as well as overall system revenue.

## File Structure

The project is modularized into several Python files for better organization:

*   `main (1).py`: The main entry point of the application containing the interactive CLI menu.
*   `data.py`: Stores the in-memory data structures (dictionaries) for flights and reservations, including some sample data to get started.
*   `flights.py`: Contains functions to add new flights and display the current flight catalog.
*   `reservations.py`: Handles the logic for booking flights, canceling reservations, and listing all current bookings.
*   `search.py`: Contains the logic to filter and search for specific flights based on user criteria.
*   `reports.py`: Calculates and displays booking and revenue statistics.

## Prerequisites

*   Python 3.x installed on your system.

## How to Run

1. Ensure all the python files (`main (1).py`, `data.py`, `flights.py`, `reservations.py`, `search.py`, `reports.py`) are placed in the same directory.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the files.
4. Run the main script using Python:

   ```bash
   python "main (1).py"
   ```

*(Note: Depending on your system, you may need to use `python3` instead of `python`)*

## Usage

Upon running the script, you will be presented with a menu:

```text
Airline Reservation System
1. Add Flight
2. Book Flight
3. Cancel Reservation
4. Display Flights
5. Display All Reservations
6. Search Flights
7. Generate Report
8. Exit
Choose an option (1-8):
```

Simply type the number corresponding to the action you want to perform and follow the on-screen prompts.
