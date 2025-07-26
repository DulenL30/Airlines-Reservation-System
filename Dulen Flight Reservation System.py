import datetime
from typing import List, Dict


class FlightReservationSystem:
    def __init__(self):
        self.flights = []
        self.customers = []
        self.bookings = []
        
        # Default credentials
        self.username = "Staff"
        self.password = "Cloud123"
        
        # Initialize default flights
        self.initialize_default_flights()
    
    def initialize_default_flights(self):
        """Initialize the three default flights as specified in the coursework"""
        tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        
        # Default flight schedule
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
            {
                'flight_no': "JFK002",
                'departure_from': "JFK",
                'arrival_to': "Miami",
                'departure_date': tomorrow,
                'departure_time': "14:00",
                'economy_seats': 20,
                'business_seats': 20,
                'economy_fare': 500,
                'business_fare': 1000,
                'economy_booked': 0,
                'business_booked': 0
            },
            {
                'flight_no': "JFK003",
                'departure_from': "JFK",
                'arrival_to': "Los Angeles",
                'departure_date': tomorrow,
                'departure_time': "20:30",
                'economy_seats': 20,
                'business_seats': 20,
                'economy_fare': 500,
                'business_fare': 1000,
                'economy_booked': 0,
                'business_booked': 0
            }
        ]
        
        self.flights.extend(default_flights)
    
    def display_header(self, title):
        """Display a consistent header for all screens"""
        print("\n" + "="*50)
        print(f"CloudFare Airlines - {title}")
        print("="*50)
    
    def validate_date(self, date_str):
        """Validate date format (YYYY-MM-DD)"""
        try:
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    
    def validate_time(self, time_str):
        """Validate time format (HH:MM)"""
        try:
            datetime.datetime.strptime(time_str, "%H:%M")
            return True
        except ValueError:
            return False
    
    def staff_login(self):
        """Handle staff login with validation"""
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
    
    def main_menu(self):
        """Display and handle main menu options"""
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
                elif choice == 3:
                    self.search_flights()
                elif choice == 4:
                    self.book_flight()
                elif choice == 5:
                    self.view_bookings()
                elif choice == 6:
                    print("Thank you for using CloudFare Airlines!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1-6.")
            except ValueError:
                print("Please enter a valid number!")
    
    def add_flight(self):
        """Add a new flight with validation using while loops for each input"""
        self.display_header("Add Flight Details")
        
        try:
            # Flight number validation with while loop
            flight_no = ""
            while True:
                flight_no = input("Flight No (JFKxxx): ").strip().upper()
                if not (flight_no.startswith('JFK') and flight_no[3:].isdigit() and len(flight_no) == 6):
                    print("Invalid flight number format. Must be JFK followed by 3 digits (e.g., JFK001)")
                    continue
                
                if any(f['flight_no'] == flight_no for f in self.flights):
                    print("Flight number already exists!")
                    continue
                
                break  # Valid and unique flight number
            
            # Departure validation (must be JFK) with while loop
            departure_from = ""
            while True:
                departure_from = input("Departure From (must be JFK): ").strip().upper()
                if departure_from != "JFK":
                    print("All flights must depart from JFK!")
                    continue
                break
            
            # Destination validation with while loop
            arrival_to = ""
            while True:
                arrival_to = input("Arrival To (Orlando/Miami/Los Angeles): ").strip()
                if arrival_to not in ["Orlando", "Miami", "Los Angeles"]:
                    print("Invalid destination. Must be Orlando, Miami, or Los Angeles")
                    continue
                break
            
            # Date validation with while loop
            departure_date = ""
            while True:
                departure_date = input("Departure Date (YYYY-MM-DD): ").strip()
                if not self.validate_date(departure_date):
                    print("Invalid date format. Please use YYYY-MM-DD")
                    continue
                break
            
            # Time validation with while loop
            departure_time = ""
            while True:
                departure_time = input("Departure Time (HH:MM): ").strip()
                if not self.validate_time(departure_time):
                    print("Invalid time format. Please use HH:MM")
                    continue
                break
            
            # Seat and fare information with while loops
            economy_seats = 70
            business_seats = 30
            economy_fare = 500.0
            business_fare = 1000.0
            
            while True:
                try:
                    economy_seats = int(input("Economy class seats (default 70): ") or "5")
                    business_seats = int(input("Business class seats (default 30): ") or "3")
                    economy_fare = float(input("Economy class fare (default $500): $") or "500")
                    business_fare = float(input("Business class fare (default $1000): $") or "1000")
                    break
                except ValueError:
                    print("Invalid number entered for seats or fare! Please enter valid numbers.")
                    continue
            
            # Confirmation with while loop
            while True:
                confirm = input("Add this flight? (Yes/No): ").strip().lower()
                if confirm in ['yes', 'y']:
                    new_flight = {
                        'flight_no': flight_no,
                        'departure_from': departure_from,
                        'arrival_to': arrival_to,
                        'departure_date': departure_date,
                        'departure_time': departure_time,
                        'economy_seats': economy_seats,
                        'business_seats': business_seats,
                        'economy_fare': economy_fare,
                        'business_fare': business_fare,
                        'economy_booked': 0,
                        'business_booked': 0
                    }
                    
                    self.flights.append(new_flight)
                    print("Flight added successfully!")
                    break
                elif confirm in ['no', 'n']:
                    print("Flight addition cancelled.")
                    break
                else:
                    print("Please enter 'Yes' or 'No'")
                    continue
                    
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def register_customer(self):
        """Register a new customer with validation using while loops for each input"""
        self.display_header("Register Customer")
        
        try:
            # Customer ID validation with while loop
            customer_id = ""
            while True:
                customer_id = input("Customer ID (Cxxx): ").strip().upper()
                if not (customer_id.startswith('C') and customer_id[1:].isdigit() and len(customer_id) == 4):
                    print("Invalid format. Must be C followed by 3 digits (e.g., C001)")
                    continue
                
                if any(c['customer_id'] == customer_id for c in self.customers):
                    print("Customer ID already exists! Please choose another.")
                    continue
                
                break  # Valid and unique customer ID
            
            # Name validation with while loop
            name = ""
            while True:
                name = input("Full Name: ").strip()
                if not name:
                    print("Name is required!")
                    continue
                break
            
            # Passport number validation with while loop
            passport_no = ""
            while True:
                passport_no = input("Passport Number: ").strip()
                if not passport_no:
                    print("Passport number is required!")
                    continue
                break
            
            # Address validation with while loop
            address = ""
            while True:
                address = input("Address: ").strip()
                if not address:
                    print("Address is required!")
                    continue
                break
            
            # Telephone validation with while loop
            telephone = ""
            while True:
                telephone = input("Telephone Number (minimum 7 digits): ").strip()
                if not telephone.isdigit() or len(telephone) < 7:
                    print("Invalid telephone number! Must be at least 7 digits.")
                    continue
                break
            
            # Confirmation with while loop
            while True:
                confirm = input("Register this customer? (Yes/No): ").strip().lower()
                if confirm in ['yes', 'y']:
                    new_customer = {
                        'customer_id': customer_id,
                        'name': name,
                        'passport_no': passport_no,
                        'address': address,
                        'telephone': telephone
                    }
                    
                    self.customers.append(new_customer)
                    print(f"Customer {name} registered successfully with ID {customer_id}!")
                    break
                elif confirm in ['no', 'n']:
                    print("Customer registration cancelled.")
                    break
                else:
                    print("Please enter 'Yes' or 'No'")
                    continue
                    
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    def search_flights(self):
        """Search for available flights with continuous validation"""
        self.display_header("Search Available Flights")
        
        try:
            # Initialize search criteria
            departure_date = ""
            departure_time = ""
            destination = ""
            travel_class = ""
            
            # Date input with validation loop
            while True:
                departure_date = input("Departure Date (YYYY-MM-DD, press Enter to skip): ").strip()
                if departure_date == "":
                    break  # Skip if empty
                if self.validate_date(departure_date):
                    break
                print("Invalid date format. Please use YYYY-MM-DD or press Enter to skip")
            
            # Time input with validation loop
            while True:
                departure_time = input("Departure Time (HH:MM, press Enter to skip): ").strip()
                if departure_time == "":
                    break  # Skip if empty
                if self.validate_time(departure_time):
                    break
                print("Invalid time format. Please use HH:MM or press Enter to skip")
            
            # Destination input with validation loop
            while True:
                destination = input("Destination (Orlando/Miami/Los Angeles, press Enter to skip): ").strip()
                if destination == "":
                    break  # Skip if empty
                if destination in ["Orlando", "Miami", "Los Angeles"]:
                    break
                print("Invalid destination. Must be Orlando, Miami, or Los Angeles (or press Enter to skip)")
            
            # Travel class input with validation loop
            while True:
                travel_class = input("Class (Economy/Business, press Enter to skip): ").strip().lower()
                if travel_class in ["economy", "business", ""]:
                    break
                print("Invalid class. Must be Economy or Business (or press Enter to skip)")
            
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
            
            # Display results
            if not matching_flights:
                print("\nNo flights found matching your criteria.")
            else:
                print("\nAvailable Flights:")
                print("-" * 80)
                print(f"{'Flight No':<10}{'Departure':<20}{'Destination':<15}{'Economy':<15}{'Business':<15}")
                print(f"{'':<10}{'Date/Time':<20}{'':<15}{'Seats':<15}{'Seats':<15}")
                print("-" * 80)
                
                for flight in matching_flights:
                    avail_economy = flight['economy_seats'] - flight['economy_booked']
                    avail_business = flight['business_seats'] - flight['business_booked']
                    
                    # Only show if matches class filter or no filter
                    if (not travel_class) or \
                    (travel_class == "economy" and avail_economy > 0) or \
                    (travel_class == "business" and avail_business > 0):
                        
                        print(f"{flight['flight_no']:<10}"
                            f"{flight['departure_date']} {flight['departure_time']:<20}"
                            f"{flight['arrival_to']:<15}"
                            f"{avail_economy if avail_economy > 0 else 'Full':<15}"
                            f"{avail_business if avail_business > 0 else 'Full':<15}")
            
            # Continue prompt
            while True:
                choice = input("\nSearch again? (Yes/No): ").strip().lower()
                if choice in ['yes', 'y']:
                    return self.search_flights()  # Recursive call for new search
                elif choice in ['no', 'n']:
                    break
                else:
                    print("Please enter Yes or No")
                    
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            input("\nPress Enter to continue...")


    def book_flight(self):
        """Book a flight with continuous validation and prompting"""
        self.display_header("Book a Flight")
        
        try:
            # Flight selection with validation loop
            flight = None
            while True:
                flight_no = input("Flight No (or 'exit' to cancel): ").strip().upper()
                
                if flight_no.lower() == 'exit':
                    print("Booking cancelled.")
                    return
                
                flight = next((f for f in self.flights if f['flight_no'] == flight_no), None)
                
                if not flight:
                    print("Flight not found! Available flights:")
                    for f in self.flights:
                        print(f"{f['flight_no']} - {f['arrival_to']} ({f['departure_date']} {f['departure_time']})")
                    continue
                
                break  # Valid flight selected
            
            # Customer verification with validation loop
            customer = None
            while True:
                passport_no = input("Passport Number (or 'exit' to cancel): ").strip()
                
                if passport_no.lower() == 'exit':
                    print("Booking cancelled.")
                    return
                
                customer = next((c for c in self.customers if c['passport_no'] == passport_no), None)
                
                if not customer:
                    print("Customer not found! Please register first or try another passport number.")
                    continue
                
                break  # Valid customer found
            
            # Class selection with validation loop
            travel_class = ""
            while True:
                travel_class = input("Class (Economy/Business): ").strip().lower()
                
                if travel_class not in ["economy", "business"]:
                    print("Invalid class. Must be 'Economy' or 'Business'")
                    continue
                
                break  # Valid class selected
            
            # Check seat availability
            if travel_class == "economy":
                if flight['economy_booked'] >= flight['economy_seats']:
                    print("No economy seats available on this flight!")
                    input("Press Enter to continue...")
                    return
                fare = flight['economy_fare']
            else:
                if flight['business_booked'] >= flight['business_seats']:
                    print("No business seats available on this flight!")
                    input("Press Enter to continue...")
                    return
                fare = flight['business_fare']
            
            # Display booking summary
            print("\nBooking Summary:")
            print("-" * 40)
            print(f"Flight: {flight['flight_no']} to {flight['arrival_to']}")
            print(f"Date: {flight['departure_date']} at {flight['departure_time']}")
            print(f"Passenger: {customer['name']} ({passport_no})")
            print(f"Class: {travel_class.title()}")
            print(f"Fare: ${fare}")
            print("-" * 40)
            
            # Confirmation with validation loop
            while True:
                confirm = input("\nConfirm booking? (Yes/No): ").strip().lower()
                
                if confirm in ['yes', 'y']:
                    # Create booking
                    booking_id = f"B{len(self.bookings) + 1:03d}"
                    new_booking = {
                        'booking_id': booking_id,
                        'flight_no': flight['flight_no'],
                        'customer_id': customer['customer_id'],
                        'passport_no': passport_no,
                        'customer_name': customer['name'],
                        'departure_date': flight['departure_date'],
                        'departure_time': flight['departure_time'],
                        'destination': flight['arrival_to'],
                        'travel_class': travel_class,
                        'fare': fare,
                        'booking_date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    }
                    
                    # Update seat counts
                    if travel_class == "economy":
                        flight['economy_booked'] += 1
                    else:
                        flight['business_booked'] += 1
                    
                    self.bookings.append(new_booking)
                    print(f"\nBooking confirmed! Booking ID: {booking_id}")
                    break
                elif confirm in ['no', 'n']:
                    print("Booking cancelled.")
                    break
                else:
                    print("Please enter 'Yes' or 'No'")
                    continue
            
            input("\nPress Enter to continue...")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            input("Press Enter to continue...")

    

    
    def view_bookings(self):
        """View all bookings"""
        self.display_header("View Bookings")
        
        if not self.bookings:
            print("No bookings found.")
            input("Press Enter to continue...")
            return
        
        # Group bookings by date
        bookings_by_date = {}
        for booking in self.bookings:
            date = booking['departure_date']
            if date not in bookings_by_date:
                bookings_by_date[date] = []
            bookings_by_date[date].append(booking)
        
        # Display bookings for each date
        for date, date_bookings in bookings_by_date.items():
            print(f"\nDeparture Date: {date}")
            print("-" * 80)
            print(f"{'Booking ID':<12}{'Flight No':<10}{'Customer':<20}{'Class':<12}{'Fare':<10}")
            print("-" * 80)
            
            for booking in date_bookings:
                print(f"{booking['booking_id']:<12}"
                      f"{booking['flight_no']:<10}"
                      f"{booking['customer_name']:<20}"
                      f"{booking['travel_class'].title():<12}"
                      f"${booking['fare']:<10}")
        
        input("\nPress Enter to continue...")

def main():
    """Main entry point for the application"""
    system = FlightReservationSystem()
    
    print("\n" + "="*50)
    print("   CloudFare Airlines Flight Reservation System")
    print("="*50)
    
    if system.staff_login():
        system.main_menu()

if __name__ == "__main__":
    main()
