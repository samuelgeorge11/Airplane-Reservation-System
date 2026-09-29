SAMPLE_FLIGHTS = {
    "A101": {
        "source": "New York",
        "destination": "Los Angeles",
        "seats": 100,
        "booked_seats": 0,
        "date": "2024-12-01",
        "price": 250.00
    },
    "B202": {
        "source": "Chicago",
        "destination": "Miami",
        "seats": 80,
        "booked_seats": 0,
        "date": "2024-12-02",
        "price": 180.00
    }
}

flights = SAMPLE_FLIGHTS.copy()
reservations = {}
