import json
import pymongo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import db

def cors_response(data, status=200):
    """Wraps response in JsonResponse and adds CORS headers."""
    response = JsonResponse(data, status=status, safe=False)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

def api_view(allowed_methods):
    """Decorator to enforce HTTP method, bypass CSRF, handle CORS options preflight, and catch database errors."""
    def decorator(func):
        @csrf_exempt
        def wrapper(request, *args, **kwargs):
            if request.method == 'OPTIONS':
                return cors_response({"detail": "Preflight OK"})
            if request.method not in allowed_methods:
                return cors_response({"error": f"Method {request.method} not allowed. Supported: {allowed_methods}"}, status=405)
            try:
                return func(request, *args, **kwargs)
            except pymongo.errors.DuplicateKeyError as dke:
                return cors_response({"error": f"A record with this unique attribute already exists. details: {str(dke)}"}, status=400)
            except Exception as e:
                return cors_response({"error": str(e)}, status=400)
        return wrapper
    return decorator

# --- CUSTOMER ENDPOINTS ---

@api_view(['GET'])
def get_customers(request):
    customers = db.get_all('customers')
    return cors_response(customers)

@api_view(['POST'])
def add_customer(request):
    data = json.loads(request.body)
    required = ['full_name', 'email', 'phone', 'address', 'password']
    for field in required:
        if field not in data:
            return cors_response({"error": f"Missing required field: {field}"}, status=400)

    # Insert into MongoDB
    inserted = db.insert_one('customers', {
        "full_name": data['full_name'],
        "email": data['email'],
        "phone": data['phone'],
        "address": data['address'],
        "password": data['password']
    }, start_id=101)
    return cors_response(inserted, status=201)

@api_view(['PUT'])
def update_customer(request, id):
    data = json.loads(request.body)
    required = ['full_name', 'email', 'phone', 'address', 'password']
    for field in required:
        if field not in data:
            return cors_response({"error": f"Missing required field: {field}"}, status=400)

    # Check if exists
    exists = db.get_one('customers', {"customer_id": id})
    if not exists:
        return cors_response({"error": f"Customer with id {id} not found"}, status=404)

    updated = db.update_one('customers', {"customer_id": id}, {
        "full_name": data['full_name'],
        "email": data['email'],
        "phone": data['phone'],
        "address": data['address'],
        "password": data['password']
    })
    return cors_response(updated)

@api_view(['DELETE'])
def delete_customer(request, id):
    exists = db.get_one('customers', {"customer_id": id})
    if not exists:
        return cors_response({"error": f"Customer with id {id} not found"}, status=404)
    db.delete_one('customers', {"customer_id": id})
    return cors_response({"success": True, "message": f"Customer with id {id} deleted successfully"})


# --- DRIVER ENDPOINTS ---

@api_view(['GET'])
def get_drivers(request):
    drivers = db.get_all('drivers')
    return cors_response(drivers)

@api_view(['POST'])
def add_driver(request):
    data = json.loads(request.body)
    required = ['driver_name', 'email', 'phone', 'license_number', 'experience', 'availability']
    for field in required:
        if field not in data:
            return cors_response({"error": f"Missing required field: {field}"}, status=400)

    inserted = db.insert_one('drivers', {
        "driver_name": data['driver_name'],
        "email": data['email'],
        "phone": data['phone'],
        "license_number": data['license_number'],
        "experience": int(data['experience']),
        "availability": data['availability']
    }, start_id=201)
    return cors_response(inserted, status=201)

@api_view(['PUT'])
def update_driver(request, id):
    data = json.loads(request.body)
    required = ['driver_name', 'email', 'phone', 'license_number', 'experience', 'availability']
    for field in required:
        if field not in data:
            return cors_response({"error": f"Missing required field: {field}"}, status=400)

    exists = db.get_one('drivers', {"driver_id": id})
    if not exists:
        return cors_response({"error": f"Driver with id {id} not found"}, status=404)

    updated = db.update_one('drivers', {"driver_id": id}, {
        "driver_name": data['driver_name'],
        "email": data['email'],
        "phone": data['phone'],
        "license_number": data['license_number'],
        "experience": int(data['experience']),
        "availability": data['availability']
    })
    return cors_response(updated)

@api_view(['DELETE'])
def delete_driver(request, id):
    exists = db.get_one('drivers', {"driver_id": id})
    if not exists:
        return cors_response({"error": f"Driver with id {id} not found"}, status=404)
    db.delete_one('drivers', {"driver_id": id})
    return cors_response({"success": True, "message": f"Driver with id {id} deleted successfully"})


# --- VEHICLE ENDPOINTS ---

@api_view(['GET'])
def get_vehicles(request):
    vehicles = db.get_all('vehicles')
    return cors_response(vehicles)

@api_view(['POST'])
def add_vehicle(request):
    data = json.loads(request.body)
    required = ['driver_name', 'vehicle_type', 'vehicle_number', 'seating_capacity', 'model']
    for field in required:
        if field not in data:
            return cors_response({"error": f"Missing required field: {field}"}, status=400)

    inserted = db.insert_one('vehicles', {
        "driver_name": data['driver_name'],
        "vehicle_type": data['vehicle_type'],
        "vehicle_number": data['vehicle_number'],
        "seating_capacity": int(data['seating_capacity']),
        "model": data['model']
    }, start_id=301)
    return cors_response(inserted, status=201)

@api_view(['PUT'])
def update_vehicle(request, id):
    data = json.loads(request.body)
    required = ['driver_name', 'vehicle_type', 'vehicle_number', 'seating_capacity', 'model']
    for field in required:
        if field not in data:
            return cors_response({"error": f"Missing required field: {field}"}, status=400)

    exists = db.get_one('vehicles', {"vehicle_id": id})
    if not exists:
        return cors_response({"error": f"Vehicle with id {id} not found"}, status=404)

    updated = db.update_one('vehicles', {"vehicle_id": id}, {
        "driver_name": data['driver_name'],
        "vehicle_type": data['vehicle_type'],
        "vehicle_number": data['vehicle_number'],
        "seating_capacity": int(data['seating_capacity']),
        "model": data['model']
    })
    return cors_response(updated)

@api_view(['DELETE'])
def delete_vehicle(request, id):
    exists = db.get_one('vehicles', {"vehicle_id": id})
    if not exists:
        return cors_response({"error": f"Vehicle with id {id} not found"}, status=404)
    db.delete_one('vehicles', {"vehicle_id": id})
    return cors_response({"success": True, "message": f"Vehicle with id {id} deleted successfully"})


# --- RIDE BOOKING ENDPOINTS ---

@api_view(['GET'])
def get_bookings(request):
    bookings = db.get_all('bookings')
    return cors_response(bookings)

@api_view(['POST'])
def add_booking(request):
    data = json.loads(request.body)
    required = ['customer_name', 'driver_name', 'pickup_location', 'drop_location', 'booking_date', 'fare', 'ride_status']
    for field in required:
        if field not in data:
            return cors_response({"error": f"Missing required field: {field}"}, status=400)

    inserted = db.insert_one('bookings', {
        "customer_name": data['customer_name'],
        "driver_name": data['driver_name'],
        "pickup_location": data['pickup_location'],
        "drop_location": data['drop_location'],
        "booking_date": data['booking_date'],
        "fare": float(data['fare']),
        "ride_status": data['ride_status']
    }, start_id=401)
    return cors_response(inserted, status=201)

@api_view(['PUT'])
def update_booking(request, id):
    data = json.loads(request.body)
    required = ['customer_name', 'driver_name', 'pickup_location', 'drop_location', 'booking_date', 'fare', 'ride_status']
    for field in required:
        if field not in data:
            return cors_response({"error": f"Missing required field: {field}"}, status=400)

    exists = db.get_one('bookings', {"booking_id": id})
    if not exists:
        return cors_response({"error": f"Booking with id {id} not found"}, status=404)

    updated = db.update_one('bookings', {"booking_id": id}, {
        "customer_name": data['customer_name'],
        "driver_name": data['driver_name'],
        "pickup_location": data['pickup_location'],
        "drop_location": data['drop_location'],
        "booking_date": data['booking_date'],
        "fare": float(data['fare']),
        "ride_status": data['ride_status']
    })
    return cors_response(updated)

@api_view(['DELETE'])
def delete_booking(request, id):
    exists = db.get_one('bookings', {"booking_id": id})
    if not exists:
        return cors_response({"error": f"Booking with id {id} not found"}, status=404)
    db.delete_one('bookings', {"booking_id": id})
    return cors_response({"success": True, "message": f"Booking with id {id} deleted successfully"})


# --- PAYMENT ENDPOINTS ---

@api_view(['GET'])
def get_payments(request):
    payments = db.get_all('payments')
    return cors_response(payments)

@api_view(['POST'])
def add_payment(request):
    data = json.loads(request.body)
    required = ['booking_id', 'customer_name', 'amount', 'payment_method', 'payment_status', 'transaction_id', 'payment_date']
    for field in required:
        if field not in data:
            return cors_response({"error": f"Missing required field: {field}"}, status=400)

    inserted = db.insert_one('payments', {
        "booking_id": int(data['booking_id']),
        "customer_name": data['customer_name'],
        "amount": float(data['amount']),
        "payment_method": data['payment_method'],
        "payment_status": data['payment_status'],
        "transaction_id": data['transaction_id'],
        "payment_date": data['payment_date']
    }, start_id=501)
    return cors_response(inserted, status=201)

@api_view(['PUT'])
def update_payment(request, id):
    data = json.loads(request.body)
    required = ['booking_id', 'customer_name', 'amount', 'payment_method', 'payment_status', 'transaction_id', 'payment_date']
    for field in required:
        if field not in data:
            return cors_response({"error": f"Missing required field: {field}"}, status=400)

    exists = db.get_one('payments', {"payment_id": id})
    if not exists:
        return cors_response({"error": f"Payment with id {id} not found"}, status=404)

    updated = db.update_one('payments', {"payment_id": id}, {
        "booking_id": int(data['booking_id']),
        "customer_name": data['customer_name'],
        "amount": float(data['amount']),
        "payment_method": data['payment_method'],
        "payment_status": data['payment_status'],
        "transaction_id": data['transaction_id'],
        "payment_date": data['payment_date']
    })
    return cors_response(updated)

@api_view(['DELETE'])
def delete_payment(request, id):
    exists = db.get_one('payments', {"payment_id": id})
    if not exists:
        return cors_response({"error": f"Payment with id {id} not found"}, status=404)
    db.delete_one('payments', {"payment_id": id})
    return cors_response({"success": True, "message": f"Payment with id {id} deleted successfully"})


# --- ADMIN ENDPOINTS ---

@api_view(['GET'])
def get_admins(request):
    admins = db.get_all('admins')
    return cors_response(admins)

@api_view(['POST'])
def add_admin(request):
    data = json.loads(request.body)
    required = ['full_name', 'email', 'phone', 'password']
    for field in required:
        if field not in data:
            return cors_response({"error": f"Missing required field: {field}"}, status=400)

    inserted = db.insert_one('admins', {
        "full_name": data['full_name'],
        "email": data['email'],
        "phone": data['phone'],
        "password": data['password']
    }, start_id=901)
    return cors_response(inserted, status=201)

@api_view(['PUT'])
def update_admin(request, id):
    data = json.loads(request.body)
    required = ['full_name', 'email', 'phone', 'password']
    for field in required:
        if field not in data:
            return cors_response({"error": f"Missing required field: {field}"}, status=400)

    exists = db.get_one('admins', {"admin_id": id})
    if not exists:
        return cors_response({"error": f"Admin with id {id} not found"}, status=404)

    updated = db.update_one('admins', {"admin_id": id}, {
        "full_name": data['full_name'],
        "email": data['email'],
        "phone": data['phone'],
        "password": data['password']
    })
    return cors_response(updated)

@api_view(['DELETE'])
def delete_admin(request, id):
    exists = db.get_one('admins', {"admin_id": id})
    if not exists:
        return cors_response({"error": f"Admin with id {id} not found"}, status=404)
    db.delete_one('admins', {"admin_id": id})
    return cors_response({"success": True, "message": f"Admin with id {id} deleted successfully"})

