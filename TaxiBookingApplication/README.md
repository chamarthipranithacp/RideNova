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

## Postman Screenshots

Module	API	Method
Customer	/customers/add/	POST
<img width="959" height="539" alt="image" src="https://github.com/user-attachments/assets/8bf0bc84-84bb-4017-8758-3dc45f2770d1" />

Driver	/drivers/	GET
<img width="959" height="539" alt="image" src="https://github.com/user-attachments/assets/1b36d5ed-34bd-4df3-aee8-d3a0bbe7864b" />

Vehicle	/vehicles/	GET
<img width="959" height="539" alt="image" src="https://github.com/user-attachments/assets/9bae6762-eb3e-491a-8dd8-6b918889d072" />

Booking	/bookings/	GET
<img width="959" height="539" alt="image" src="https://github.com/user-attachments/assets/266670b4-0602-4572-9ea9-82fe8fb8f5c8" />

Payment	/payments/	GET
<img width="959" height="539" alt="image" src="https://github.com/user-attachments/assets/a750cf85-e6ac-4b4f-9330-41ccd6cafdde" />

## Frontend Screenshots

🏠 Home Page (index.html)
<img width="957" height="476" alt="image" src="https://github.com/user-attachments/assets/c115093a-1fb2-49de-995b-94a601afac93" />

👤 Register Page (register.html)
<img width="491" height="420" alt="image" src="https://github.com/user-attachments/assets/2f6a2c42-339c-4393-83e6-63164e39eb13" />

🔑 Login Page (login.html)
<img width="698" height="427" alt="image" src="https://github.com/user-attachments/assets/45f57017-1633-49df-a701-d574a6dcd2f5" />

🚖 Ride Booking Page (booking.html)
<img width="674" height="434" alt="image" src="https://github.com/user-attachments/assets/506f1edb-78a9-480b-a829-b638d81842f4" />

👨‍✈️ Driver Page (drivers.html)
<img width="679" height="431" alt="image" src="https://github.com/user-attachments/assets/ede4ba71-d134-4f08-8322-ef0599069449" />

💳 Payment Page (payments.html)
<img width="298" height="349" alt="image" src="https://github.com/user-attachments/assets/2b64edb0-9bc3-4cd4-97f8-f081f187f1be" />

📜 Ride History (ride_history.html)
<img width="884" height="425" alt="image" src="https://github.com/user-attachments/assets/d99603c1-b8fa-4651-88e2-dd3febb45cdd" />

📊 Customer Dashboard (customer_dashboard.html)
<img width="957" height="434" alt="image" src="https://github.com/user-attachments/assets/b080f182-d6e0-4300-93dc-40cbff188f56" />

🚕 Driver Dashboard (driver_dashboard.html)
<img width="955" height="437" alt="image" src="https://github.com/user-attachments/assets/ee04754c-9301-47f1-984c-f3c00640497e" />

🛠️ Admin Dashboard (admin_dashboard.html)
<img width="745" height="376" alt="image" src="https://github.com/user-attachments/assets/484e053f-22ee-4e59-a545-630dfd894710" />

The RideNova Taxi Booking Application was successfully developed using HTML, CSS, JavaScript, Django REST APIs, and MySQL. The project includes Customer, Driver, Vehicle, Booking, Payment, and Admin modules with complete CRUD operations. All APIs were tested successfully using Postman, and the frontend was verified through browser testing. The attached Postman API screenshots and frontend screenshots demonstrate the successful implementation, functionality, and user-friendly interface of the RideNova application.
