import psycopg2
from time import perf_counter

# CONSTANTS
DB_NAME = "database name"                                           # REPLACE WITH PostgreSQL database name
USER = "username"                                                   # REPLACE WITH PostgreSQL user
PASSWORD = "password"                                               # REPLACE WITH PostgreSQL password
PORT = "5432"                                                       # REPLACE WITH PostgreSQL port

MOVIES_TABLE = "C:/movies.csv"                                      # REPLACE WITH movies.csv ABSOLUTE PATH
RATINGS_TABLE = "C:/ratings.csv"                                    # REPLACE WITH ratings.csv ABSOLUTE PATH

# TEST
if __name__ == "__main__":
    # Establish Connection to Database
    conn = psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, port=PORT)

    # Open a cursor
    cur = conn.cursor()

    try:
        # Dropping existing tables
        cur.execute('''
        DROP TABLE IF EXISTS ratings, movies;
        ''')

        # Creating Tables
        cur.execute('''
        CREATE TABLE movies (
            movieId INT PRIMARY KEY,
            title VARCHAR(255),
            genres VARCHAR(255)
        );
        ''')

        cur.execute('''
        CREATE TABLE ratings (
            userId INT,
            movieId INT,
            rating REAL,
            timestamp BIGINT,
            PRIMARY KEY (userId, movieId),
            FOREIGN KEY (movieId) REFERENCES movies(movieId)
        )
        ''')
        # Commit creation
        conn.commit()

        # Inserting data
        cur.execute(f'''
        COPY movies(movieId, title, genres)
        FROM '{MOVIES_TABLE}'
        DELIMITER ','
        CSV HEADER;
        ''')

        write_clock_start = perf_counter()
        cur.execute(f'''
        COPY ratings(userId,movieId,rating,timestamp)
        FROM '{RATINGS_TABLE}'
        DELIMITER ','
        CSV HEADER;
        ''')
        write_clock_end = perf_counter()
        print(f'WRITE 10.000 DATA EXECUTION TIME: {write_clock_end - write_clock_start} seconds')

        # Commit insertion
        conn.commit()

        # Reading data
        read_clock_start = perf_counter()
        cur.execute(f'''
        SELECT *
        FROM ratings
        LIMIT 10000;
        ''')
        read_clock_end = perf_counter()
        print(f'READ 10.000 DATA EXECUTION TIME: {read_clock_end - read_clock_start} seconds')

    except Exception as e:
        # Exception handling
        print("Process interrupted")
        print(e)

    finally:
        # Commit Changes
        conn.commit()
        # Close connection
        cur.close()
        conn.close()