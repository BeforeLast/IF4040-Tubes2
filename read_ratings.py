from get_database import get_database
import time
import pandas as pd
dbname = get_database()
#load the database collection
collection_name = dbname["ratings"]

#print(data)
st = time.perf_counter()
arr = list(collection_name.find())
et = time.perf_counter()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')