# Flight Reservation System

## 🎯 Project Overview

This comprehensive flight reservation system is your one-stop solution for managing flights, customers, and bookings. Built with Python's elegance and designed with user experience in mind, this system handles everything from flight scheduling to customer management with style.

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

```python
def __init__(self):
    self.flights = []
    self.customers = []
    self.bookings = []
    
    # Default credentials
    self.username = "Staff"
    self.password = "Cloud123"
    
    # Initialize default flights
    self.initialize_default_flights()
```

### `initialize_default_flights()`
Creates three default flights (JFK001, JFK002, JFK003) departing tomorrow to Orlando, Miami, and Los Angeles respectively. Each flight has 20 economy and 20 business class seats.

```python
def initialize_default_flights(self):
    tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    
    default_flights = [
        {
            'flight_no': "JFK001",
            'departure_from': "JFK",
            'arrival_to': "Orlando",
            'departure_date': tomorrow,
            'departure_time': "06:30",
            'economy_seats': 20,
            'business_seats': 20,
            'economy_fare': 500,
            'business_fare': 1000,
            'economy_booked': 0,
            'business_booked': 0
        },
        # Similar structure for JFK002 and JFK003
    ]
    
    self.flights.extend(default_flights)
```

### `display_header(title)`
Displays a consistent formatted header across all system screens with the CloudFare Airlines branding and the current screen title.

```python
def display_header(self, title):
    print("\n" + "="*50)
    print(f"CloudFare Airlines - {title}")
    print("="*50)
```

### `validate_date(date_str)` & `validate_time(time_str)`
Input validation functions that ensure dates follow YYYY-MM-DD format and times follow HH:MM format using datetime parsing.

```python
def validate_date(self, date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_time(self, time_str):
    try:
        datetime.datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False
```

### `staff_login()`
Handles secure staff authentication. Prompts for username and password, validates against stored credentials, and provides retry options on failed attempts.

```python
def staff_login(self):
    self.display_header("Staff Login")
    
    while True:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if username == self.username and password == self.password:
            print("\nLogin successful!")
            return True
        
        choice = input("Login failed. Try again? (Yes/No): ").strip().lower()
        if choice not in ['yes', 'y']:
            return False
```

### `main_menu()`
Core navigation hub that displays the main menu options and routes user selections to appropriate functions. Includes error handling for invalid menu choices.

```python
def main_menu(self):
    while True:
        self.display_header("Main Menu")
        print("1. Add flight details")
        print("2. Register a customer")
        print("3. Search for available flights")
        print("4. Book a flight")
        print("5. View booking details")
        print("6. Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-6): "))
            
            if choice == 1:
                self.add_flight()
            elif choice == 2:
                self.register_customer()
            # ... other menu options
        except ValueError:
            print("Please enter a valid number!")
```

### `add_flight()`
Comprehensive flight creation function with step-by-step validation:
- Validates flight number format (JFKxxx)
- Ensures departure is from JFK
- Validates destination (Orlando/Miami/Los Angeles)
- Validates date and time formats
- Collects seat and fare information
- Prevents duplicate flight numbers

```python
def add_flight(self):
    self.display_header("Add Flight Details")
    
    # Flight number validation with while loop
    flight_no = ""
    while True:
        flight_no = input("Flight No (JFKxxx): ").strip().upper()
        if not (flight_no.startswith('JFK') and flight_no[3:].isdigit() and len(flight_no) == 6):
            print("Invalid flight number format. Must be JFK followed by 3 digits")
            continue
        
        if any(f['flight_no'] == flight_no for f in self.flights):
            print("Flight number already exists!")
            continue
        
        break  # Valid and unique flight number
    
    # Similar validation patterns for other inputs...
```

### `register_customer()`
Customer registration system with complete validation:
- Validates customer ID format (Cxxx)
- Collects full passenger details
- Validates passport information
- Ensures unique customer IDs
- Validates telephone numbers (minimum 7 digits)

```python
def register_customer(self):
    self.display_header("Register Customer")
    
    # Customer ID validation with while loop
    customer_id = ""
    while True:
        customer_id = input("Customer ID (Cxxx): ").strip().upper()
        if not (customer_id.startswith('C') and customer_id[1:].isdigit() and len(customer_id) == 4):
            print("Invalid format. Must be C followed by 3 digits")
            continue
        
        if any(c['customer_id'] == customer_id for c in self.customers):
            print("Customer ID already exists!")
            continue
        
        break
    
    # Collect other customer details with validation...
```

### `search_flights()`
Flexible flight search engine that allows filtering by:
- Departure date
- Departure time
- Destination
- Travel class (Economy/Business)
- Displays real-time seat availability
- Supports partial search criteria

```python
def search_flights(self):
    self.display_header("Search Available Flights")
    
    # Collect search criteria with validation
    departure_date = input("Departure Date (YYYY-MM-DD, press Enter to skip): ").strip()
    departure_time = input("Departure Time (HH:MM, press Enter to skip): ").strip()
    destination = input("Destination (Orlando/Miami/Los Angeles, press Enter to skip): ").strip()
    
    # Find matching flights
    matching_flights = []
    for flight in self.flights:
        match = True
        
        if departure_date and flight['departure_date'] != departure_date:
            match = False
        if departure_time and flight['departure_time'] != departure_time:
            match = False
        if destination and flight['arrival_to'] != destination:
            match = False
        
        if match:
            matching_flights.append(flight)
    
    # Display results in formatted table...
```

### `book_flight()`
Complete booking process with validation:
- Flight selection and verification
- Customer authentication via passport
- Class selection (Economy/Business)
- Seat availability checking
- Booking confirmation with unique ID generation
- Automatic seat count updates

```python
def book_flight(self):
    self.display_header("Book a Flight")
    
    # Flight selection
    flight_no = input("Flight No (or 'exit' to cancel): ").strip().upper()
    flight = next((f for f in self.flights if f['flight_no'] == flight_no), None)
    
    if not flight:
        print("Flight not found!")
        return
    
    # Customer verification
    passport_no = input("Passport Number: ").strip()
    customer = next((c for c in self.customers if c['passport_no'] == passport_no), None)
    
    # Create booking with unique ID
    booking_id = f"B{len(self.bookings) + 1:03d}"
    new_booking = {
        'booking_id': booking_id,
        'flight_no': flight['flight_no'],
        'customer_id': customer['customer_id'],
        # ... other booking details
    }
    
    self.bookings.append(new_booking)
```

### `view_bookings()`
Comprehensive booking display system:
- Groups bookings by departure date
- Shows detailed booking information
- Displays customer names, flight details, and fares
- Organized tabular format for easy reading

```python
def view_bookings(self):
    self.display_header("View Bookings")
    
    if not self.bookings:
        print("No bookings found.")
        return
    
    # Group bookings by date
    bookings_by_date = {}
    for booking in self.bookings:
        date = booking['departure_date']
        if date not in bookings_by_date:
            bookings_by_date[date] = []
        bookings_by_date[date].append(booking)
    
    # Display formatted booking information
    for date, date_bookings in bookings_by_date.items():
        print(f"\nDeparture Date: {date}")
        print("-" * 80)
        # Print tabular booking details...
```

### `main()`
Application entry point that initializes the system, displays welcome message, handles staff login, and launches the main menu interface.

```python
def main():
    system = FlightReservationSystem()
    
    print("\n" + "="*50)
    print("   CloudFare Airlines Flight Reservation System")
    print("="*50)
    
    if system.staff_login():
        system.main_menu()

if __name__ == "__main__":
    main()
```

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




