from  pymongo import MongoClient


class DatabaseConnection:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        self.connection = f"Connected to {self.host}:{self.port} as {self.username}"
        mongo_client = MongoClient(self.host, self.port, username=self.username, password=self.password)
        return mongo_client
    def disconnect(self, mongo_client):   
        mongo_client.close()
        return "Disconnected from MongoDB"
    
    def get_database(self, mongo_client, database_name):
        db = mongo_client[database_name]
        return db
    
    def get_collection(self, mongo_client, database_name, collection_name):
        db = mongo_client[database_name]
        collection = db[collection_name]
        return collection
    
    def create_collection(self, mongo_client, database_name, collection_name):
        db = mongo_client[database_name]
        collection = db[collection_name]
        return collection

    def insert_data(self, mongo_client, database_name, collection_name, data):
        db = mongo_client[database_name]
        collection = db[collection_name]
        result = collection.insert_one(data)
        return f"Data inserted with id: {result.inserted_id}"
    def get_data(self, mongo_client, database_name, collection_name, query):
        db = mongo_client[database_name]
        collection = db[collection_name]
        result = collection.find(query)
        return list(result)
    def update_data(self, mongo_client, database_name, collection_name, query, new_values):
        db = mongo_client[database_name]
        collection = db[collection_name]
        result = collection.update_one(query, {"$set": new_values})
        return f"Matched {result.matched_count} documents and modified {result.modified_count} documents"
    def delete_data(self, mongo_client, database_name, collection_name, query):
        db = mongo_client[database_name]
        collection = db[collection_name]
        result = collection.delete_one(query)
        return f"Deleted {result.deleted_count} documents"
    

