# Airlines Flight Reservation System

## 🎯 Project Overview

Welcome aboard CloudFare Airlines! This comprehensive flight reservation system is your one-stop solution for managing flights, customers, and bookings. Built with Python's elegance and designed with user experience in mind, this system handles everything from flight scheduling to customer management with style.

## ✨ Features

### 🔐 Secure Staff Access
- Protected login system with default credentials
- Username: `Staff` | Password: `Cloud123`

### ✈️ Flight Management
- **Pre-loaded Routes**: Three default flights ready to go!
  - **JFK001**: JFK → Orlando (06:30)
  - **JFK002**: JFK → Miami (14:00) 
  - **JFK003**: JFK → Los Angeles (20:30)
- **Add New Flights**: Expand your airline empire
- **Smart Validation**: JFK-format flight numbers, proper date/time formats

### 👥 Customer Registration
- Customer ID format: `Cxxx` (e.g., C001)
- Complete passenger profiles with passport details
- Address and contact information management

### 🔍 Intelligent Flight Search
- Search by date, time, destination, or class
- Real-time seat availability
- Flexible filtering options

### 🎫 Seamless Booking System
- Two-class service: Economy & Business
- Automatic seat allocation
- Booking confirmation with unique IDs
- Real-time fare calculation

### 📊 Comprehensive Booking Management
- View all bookings organized by departure date
- Detailed passenger information
- Flight and fare summaries

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.6 or higher
```

### Installation & Launch
```bash
# Clone or download the project
# Navigate to project directory
cd cloudfare-airlines

# Run the system
python flight_reservation_system.py
```

## 🎮 How to Use

### 1. Staff Login
```
Username: Staff
Password: Cloud123
```

### 2. Main Menu Navigation
```
1. Add flight details      - Expand your flight network
2. Register a customer     - Add new passengers  
3. Search for flights      - Find available options
4. Book a flight          - Complete reservations
5. View booking details   - Review all bookings
6. Exit                   - Safe departure
```

### 3. Input Formats
- **Flight Numbers**: `JFKxxx` (e.g., JFK001, JFK999)
- **Customer IDs**: `Cxxx` (e.g., C001, C123)
- **Dates**: `YYYY-MM-DD` (e.g., 2024-12-25)
- **Times**: `HH:MM` (e.g., 14:30, 09:15)
- **Destinations**: Orlando, Miami, Los Angeles

## 🏗️ System Architecture

```
FlightReservationSystem/
├── Authentication Module
├── Flight Management
├── Customer Registration  
├── Search Engine
├── Booking System
└── Reporting Dashboard
```

## 💾 Data Structure

### Flight Object
```python
{
    'flight_no': 'JFK001',
    'departure_from': 'JFK',
    'arrival_to': 'Orlando',
    'departure_date': '2024-07-27',
    'departure_time': '06:30',
    'economy_seats': 20,
    'business_seats': 20,
    'economy_fare': 500,
    'business_fare': 1000
}
```

### Customer Profile
```python
{
    'customer_id': 'C001',
    'name': 'John Doe',
    'passport_no': 'AB123456',
    'address': '123 Main St',
    'telephone': '1234567890'
}
```

## 🔧 Core Functions

### `__init__()`
Initializes the flight reservation system with empty lists for flights, customers, and bookings. Sets up default staff credentials and loads three pre-configured flights for the next day.

### `initialize_default_flights()`
Creates three default flights (JFK001, JFK002, JFK003) departing tomorrow to Orlando, Miami, and Los Angeles respectively. Each flight has 20 economy and 20 business class seats.

### `display_header(title)`
Displays a consistent formatted header across all system screens with the CloudFare Airlines branding and the current screen title.

### `validate_date(date_str)` & `validate_time(time_str)`
Input validation functions that ensure dates follow YYYY-MM-DD format and times follow HH:MM format using datetime parsing.

### `staff_login()`
Handles secure staff authentication. Prompts for username and password, validates against stored credentials, and provides retry options on failed attempts.

### `main_menu()`
Core navigation hub that displays the main menu options and routes user selections to appropriate functions. Includes error handling for invalid menu choices.

### `add_flight()`
Comprehensive flight creation function with step-by-step validation:
- Validates flight number format (JFKxxx)
- Ensures departure is from JFK
- Validates destination (Orlando/Miami/Los Angeles)
- Validates date and time formats
- Collects seat and fare information
- Prevents duplicate flight numbers

### `register_customer()`
Customer registration system with complete validation:
- Validates customer ID format (Cxxx)
- Collects full passenger details
- Validates passport information
- Ensures unique customer IDs
- Validates telephone numbers (minimum 7 digits)

### `search_flights()`
Flexible flight search engine that allows filtering by:
- Departure date
- Departure time
- Destination
- Travel class (Economy/Business)
- Displays real-time seat availability
- Supports partial search criteria

### `book_flight()`
Complete booking process with validation:
- Flight selection and verification
- Customer authentication via passport
- Class selection (Economy/Business)
- Seat availability checking
- Booking confirmation with unique ID generation
- Automatic seat count updates

### `view_bookings()`
Comprehensive booking display system:
- Groups bookings by departure date
- Shows detailed booking information
- Displays customer names, flight details, and fares
- Organized tabular format for easy reading

### `main()`
Application entry point that initializes the system, displays welcome message, handles staff login, and launches the main menu interface.

## 🛡️ Error Handling & Validation

- **Robust Input Validation**: All user inputs are validated with clear error messages
- **Duplicate Prevention**: Prevents duplicate flight numbers and customer IDs
- **Format Enforcement**: Ensures proper date, time, and ID formats
- **Graceful Error Recovery**: User-friendly error messages with retry options

## 🌟 Unique Features

- **Continuous Validation**: Never lose your progress due to input errors
- **Smart Defaults**: Pre-configured with tomorrow's flights
- **Flexible Search**: Search with any combination of criteria
- **Organized Display**: Bookings grouped by departure date
- **Secure Operations**: Staff authentication required

## 🛠️ Technical Specifications

- **Language**: Python 3.6+
- **Libraries**: `datetime`, `typing`
- **Architecture**: Object-Oriented Design
- **Data Storage**: In-memory (runtime persistence)
- **Interface**: Command-Line Interface (CLI)


