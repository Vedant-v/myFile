from pymongo import MongoClient

client = MongoClient('localhost', 27017, username='vedant', password='VedantKulkani@123')
db = client['mydatabase']
collection = db['mycollection']
multyple_data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "David", "age": 28, "city": "Houston"},
    {"name": "Eve", "age": 22, "city": "Phoenix"}
]
result = collection.insert_many(multyple_data)

for doc in collection.find():
    print(doc)