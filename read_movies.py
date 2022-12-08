from get_database import get_database
import time
import pandas as pd
dbname = get_database()
#load the database collection
collection_name = dbname["movies"]

st = time.perf_counter()
print(collection_name.find())
et = time.perf_counter()
elapsed_time = et - st
print('Execution time (cursor only):', elapsed_time, 'seconds')

#print(data)
st = time.perf_counter()
arr = list(collection_name.find())
et = time.perf_counter()
elapsed_time = et - st
print('Execution time (turn to list):', elapsed_time, 'seconds')