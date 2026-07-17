import os
import pymongo
from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://chamarthipranithacp_db_user:Padhu%402005@cluster0.jahnd1x.mongodb.net/"

# Module-level connection
client = MongoClient(CONNECTION_STRING)
db = client['taxi_booking']

def clean_doc(doc):
    """Converts MongoDB ObjectId to string to make the document JSON serializable."""
    if doc:
        if '_id' in doc:
            doc['_id'] = str(doc['_id'])
    return doc

def clean_docs(docs):
    return [clean_doc(doc) for doc in docs]

def get_next_id(collection_name, start_id):
    """Generates the next integer ID for a custom collection ID field."""
    col = db[collection_name]
    id_field = collection_name[:-1] + "_id"  # e.g., "customers" -> "customer_id"
    last_item = col.find_one(sort=[(id_field, -1)])
    if last_item:
        return last_item[id_field] + 1
    return start_id

def init_db():
    """Seeds the MongoDB collections if they are empty and sets unique indices."""
    try:
        # Seed Customers
        customers_col = db['customers']
        if customers_col.count_documents({}) == 0:
            customers_col.insert_one({
                "customer_id": 101,
                "full_name": "Rahul Sharma",
                "email": "rahul@gmail.com",
                "phone": "9876543210",
                "address": "Hyderabad",
                "password": "rahul123"
            })
        # Create unique index on email
        customers_col.create_index("email", unique=True)

        # Seed Drivers
        drivers_col = db['drivers']
        if drivers_col.count_documents({}) == 0:
            drivers_col.insert_one({
                "driver_id": 201,
                "driver_name": "Ramesh Kumar",
                "email": "ramesh@gmail.com",
                "phone": "9988776655",
                "license_number": "DL123456789",
                "experience": 5,
                "availability": "Available"
            })
        drivers_col.create_index("email", unique=True)

        # Seed Vehicles
        vehicles_col = db['vehicles']
        if vehicles_col.count_documents({}) == 0:
            vehicles_col.insert_one({
                "vehicle_id": 301,
                "driver_name": "Ramesh Kumar",
                "vehicle_type": "Sedan",
                "vehicle_number": "TS09AB1234",
                "seating_capacity": 4,
                "model": "Hyundai Verna"
            })
        vehicles_col.create_index("vehicle_number", unique=True)

        # Seed Bookings
        bookings_col = db['bookings']
        if bookings_col.count_documents({}) == 0:
            bookings_col.insert_one({
                "booking_id": 401,
                "customer_name": "Rahul Sharma",
                "driver_name": "Ramesh Kumar",
                "pickup_location": "Madhapur",
                "drop_location": "Gachibowli",
                "booking_date": "2026-08-15",
                "fare": 350.0,
                "ride_status": "Accepted"
            })

        # Seed Payments
        payments_col = db['payments']
        if payments_col.count_documents({}) == 0:
            payments_col.insert_one({
                "payment_id": 501,
                "booking_id": 401,
                "customer_name": "Rahul Sharma",
                "amount": 350.0,
                "payment_method": "UPI",
                "payment_status": "Success",
                "transaction_id": "TXN456789123",
                "payment_date": "2026-08-15"
            })

        # Seed Admins
        admins_col = db['admins']
        if admins_col.count_documents({}) == 0:
            admins_col.insert_one({
                "admin_id": 901,
                "full_name": "System Admin",
                "email": "admin",
                "phone": "0000000000",
                "password": "admin"
            })
        admins_col.create_index("email", unique=True)
        
        print("Database initialized and seeded on MongoDB Atlas.")
    except Exception as e:
        print(f"Error seeding database: {e}")

# --- CRUD Helper operations ---

def get_all(collection_name):
    col = db[collection_name]
    return clean_docs(list(col.find({})))

def get_one(collection_name, query):
    col = db[collection_name]
    return clean_doc(col.find_one(query))

def insert_one(collection_name, doc, start_id):
    col = db[collection_name]
    id_field = collection_name[:-1] + "_id"
    if id_field not in doc or doc[id_field] is None:
        doc[id_field] = get_next_id(collection_name, start_id)
    col.insert_one(doc)
    return clean_doc(doc)

def update_one(collection_name, query, update_data):
    col = db[collection_name]
    col.update_one(query, {"$set": update_data})
    return clean_doc(col.find_one(query))

def delete_one(collection_name, query):
    col = db[collection_name]
    res = col.delete_one(query)
    return res.deleted_count > 0

if __name__ == '__main__':
    init_db()
