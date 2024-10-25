from pymongo import MongoClient

def log_stats():
    # Connect to MongoDB (default URI)
    client = MongoClient("mongodb://localhost:27017/")
    
    # Access the 'logs' database and the 'nginx' collection
    db = client.logs
    collection = db.nginx
    
    # Check if the collection has documents
    total_logs = collection.count_documents({})
    
    if total_logs == 0:
        print("Collection nginx empty")
        return
    elif total_logs == 1:
        print("Collection nginx with 1 document")
    elif total_logs == 10:
        print("Collection nginx with 10 documents")
    else:
        print(f"Collection nginx with {total_logs} documents")

    # Continue with the regular flow
    print(f"{total_logs} logs")
    
    # Methods to track
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    
    # Count the logs by method
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    # Count GET requests to path /status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
