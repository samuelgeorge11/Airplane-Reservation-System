# Project Statement: Airline Reservation System

## Problem Statement
Managing flight schedules, passenger bookings, and ticket revenue manually or through overly complex enterprise software can be inefficient for small-scale operations, travel agencies, or educational environments. There is a need for a lightweight, straightforward, and easy-to-deploy system that allows operators to seamlessly add flights, manage reservations, and track basic revenue metrics without the overhead of a large-scale database or complicated user interface.

## Scope of the Project
This project is a Command Line Interface (CLI) based application developed in Python. 

**In-Scope:**
* In-memory data management for flights and reservations.
* Core CRUD (Create, Read, Update, Delete) operations for flight inventory and bookings.
* Basic search and filtering mechanisms for available flights.
* Automated calculation of available seats and revenue reporting.

**Out-of-Scope:**
* Persistent data storage (e.g., SQL/NoSQL databases).
* Graphical User Interface (GUI) or Web Interface.
* User authentication and authorization (e.g., admin vs. customer roles).
* Integration with real-time payment gateways or external airline APIs.

## Target Users
* **Ticketing Agents / Small Travel Agencies:** Users who need a quick, terminal-based tool to log bookings and check flight availability.
* **Administrative Trainees:** Airline or travel staff using the system in a simulated environment for training purposes.
* **Students and Developers:** Individuals looking for a foundational project to understand system design, modular programming, and CLI application development in Python.

## High-Level Features
* **Flight Management:** Ability to dynamically add new flights to the system with details like source, destination, capacity, date, and price, as well as display the entire flight catalog.
* **Reservation Engine:** Functionality to book passengers onto specific flights (automatically generating unique reservation IDs) and cancel existing reservations to free up seating capacity.
* **Search Functionality:** A dedicated search tool allowing users to find specific flights based on departure location, destination, and exact dates.
* **Reporting and Analytics:** An automated reporting tool that calculates and displays total bookings and revenue generated per flight, alongside the overall system revenue.