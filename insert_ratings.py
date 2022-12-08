from get_database import get_database
import time
import pandas as pd
dbname = get_database()
collection_name = dbname["ratings"]

df = pd.read_csv('data/ratings_10k.csv')
data = df.to_dict(orient="records")

#print(data)
st = time.perf_counter()
collection_name.insert_many(data)
et = time.perf_counter()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')