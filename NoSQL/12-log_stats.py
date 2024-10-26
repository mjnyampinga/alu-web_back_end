#!/usr/bin/env python3

from pymongo import MongoClient

def log_stats():
    # Connect to the MongoDB server
    client = MongoClient()
    
    # Select the database and collection
    db = client.logs
    nginx_collection = db.nginx
    
    # Get the total count of documents
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Print out the methods count
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    # Count documents where method is GET and path is /status
    status_check_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()
