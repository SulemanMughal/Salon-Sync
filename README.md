# Salon Sync

**Salon Sync** is a simple desktop application designed to streamline the appointment booking process for beauty salons and spas. Built using Python and Tkinter, it provides an intuitive graphical interface to manage appointments, track bookings, and organize salon services and stylists efficiently.

## Features

- **Book Appointments:** Quickly schedule new appointments by entering customer name, date, time, service, and stylist.
- **View Upcoming Bookings:** See a list of all upcoming appointments, organized by date and time.
- **Input Validation:** Ensures all fields are filled and formats for date and time are correct.
- **Persistent Storage:** Uses SQLite database to store and retrieve all booking data.
- **User-Friendly Interface:** Modern and clean GUI with color themes, dropdowns, and easy navigation.

## Screenshots

*(Add screenshots of the main booking window and bookings list here if available)*

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (usually bundled with Python)
- SQLite3 (usually bundled with Python)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SulemanMughal/Salon-Sync.git
   cd Salon-Sync
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *Note: If you encounter issues with `tk`, try installing `tkinter` via your OS package manager (e.g., `sudo apt-get install python3-tk` on Ubuntu).*

3. **Run the application:**
   ```bash
   python salon_booking_app.py
   ```

## Usage

- Enter the customer's name, desired date and time, select the service, and choose a stylist.
- Click **Book Appointment** to save the booking.
- All upcoming bookings will be displayed in the list at the bottom of the window.

## Project Structure

```
salon_booking_app.py   # Main application code
requirements.txt       # Required Python packages
salon_bookings.db      # SQLite database file (created on first run)
```

## Customization

- **Services and Stylists:**  
  You can update the list of services and stylists in the `salon_booking_app.py` file to match your salon's offerings.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

- **Suleman Mughal**  
  [GitHub Profile](https://github.com/SulemanMughal)

---

*Salon Sync - Making salon bookings smarter and simpler!*
