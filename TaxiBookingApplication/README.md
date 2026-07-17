# Taxi Booking Application

This project is a premium, fully responsive **Taxi Booking Application** built with HTML5, CSS3, and ES6 JavaScript on the frontend, and a **Django REST API** server powered by **MongoDB Atlas** (using the `pymongo` driver) on the backend.


## 🛠️ Technology Stack

* **Frontend**: HTML5, CSS3 (Custom design tokens, Glassmorphism, animations), JavaScript (ES6 Fetch API)
* **Backend**: Django (Function-Based Views, CORS middleware wrappers)
* **Database**: MongoDB Atlas (`pymongo` client wrapper with custom auto-increment IDs)


## 📂 Project Directory Structure

```text
TaxiBookingApplication/
├── Backend/
│   ├── __init__.py
│   ├── db.py            # MongoDB Atlas connection & CRUD helper wrappers
│   ├── settings.py      # Django settings (triggers database seeding on start)
│   ├── urls.py          # 20 API CRUD Route definitions
│   └── views.py         # 20 Django function-based API views
├── Frontend/
│   ├── index.html       # Home page (Hero, destinations, offers)
│   ├── login.html       # Sign-in portal (Customer, Driver, Admin)
│   ├── register.html    # User registration switcher
│   ├── booking.html     # Ride booking form with fare estimator
│   ├── drivers.html     # Driver console (ride acceptance, availability toggle)
│   ├── payments.html    # Checkout gateway
│   ├── ride_history.html# Previous passenger trips with payment links
│   ├── customer_dashboard.html # Passenger metric tracker
│   ├── driver_dashboard.html   # Driver metric tracker
│   ├── admin_dashboard.html    # Full CRUD panel for all 5 collections
│   ├── style.css        # Premium Dark-mode layout stylesheet
│   └── script.js        # Core API client & session manager
├── manage.py            # Django launch utility
└── README.md            # Project documentation
```


## 🔐 Credentials for Testing

To check the application locally, you can use these seeded credentials:

| Role | Email / ID | Credential |
| :--- | :--- | :--- |
| **System Administrator** | `admin` | `admin` (Password) |
| **Passenger (Customer)** | `rahul@gmail.com` | `rahul123` (Password) |
| **Driver Partner** | `ramesh@gmail.com` | `9988776655` (Phone number as credential) |


## 🌐 API Endpoint Schema (20 REST Endpoints)

### 👥 Customer Management
* **`POST /customers/add/`**: Register a customer
* **`GET /customers/`**: Fetch all customers
* **`PUT /customers/update/<id>/`**: Edit a customer
* **`DELETE /customers/delete/<id>/`**: Remove a customer

### 🚗 Driver Management
* **`POST /drivers/add/`**: Register a driver
* **`GET /drivers/`**: Fetch all drivers
* **`PUT /drivers/update/<id>/`**: Edit availability or details of a driver
* **`DELETE /drivers/delete/<id>/`**: Remove a driver

### 🚘 Vehicle Management
* **`POST /vehicles/add/`**: Add driver's vehicle info
* **`GET /vehicles/`**: Fetch all vehicles
* **`PUT /vehicles/update/<id>/`**: Edit vehicle info
* **`DELETE /vehicles/delete/<id>/`**: Remove a vehicle

### 📅 Ride Booking Management
* **`POST /bookings/add/`**: Submit a new ride booking
* **`GET /bookings/`**: Fetch all bookings
* **`PUT /bookings/update/<id>/`**: Update booking status (`Requested` ➔ `Accepted` ➔ `In Progress` ➔ `Completed` ➔ `Cancelled`)
* **`DELETE /bookings/delete/<id>/`**: Remove a booking

### 💳 Payment Management
* **`POST /payments/add/`**: Create a payment record
* **`GET /payments/`**: Fetch all payment logs
* **`PUT /payments/update/<id>/`**: Edit a payment log
* **`DELETE /payments/delete/<id>/`**: Remove a payment log

### 🛡️ Administrator Management
* **`POST /admins/add/`**: Register a new admin
* **`GET /admins/`**: Fetch all admins
* **`PUT /admins/update/<id>/`**: Edit an admin
* **`DELETE /admins/delete/<id>/`**: Remove an admin


## 🚀 How to Run the Application

### 1. Start the Django Server
From the root folder `TaxiBookingApplication/`, run:
```bash
python manage.py runserver 127.0.0.1:8000
```
Upon launching, it will automatically connect to MongoDB Atlas, create index constraints, and seed any missing sample data.

### 2. Launch the Frontend
Double-click `Frontend/index.html` to open it in a browser, or run a local web server (e.g. VS Code Live Server extension).

### 3. Verification Testing
We have included a test suite that performs automated integration assertions against all 24 API CRUD endpoints:
```bash
python test_apis.py
```
*(Located in the workspace artifacts/scratch directory).*
