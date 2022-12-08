from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(os.getenv('CONNECTION_STRING'))
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['my-new-db-2']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()