import psycopg2
try:
    connection = psycopg2.connect(
        database="portfoliodb",
        user="andrauritu",
        password="numauita",
        host="127.0.0.1",
        port="5432"
    )
    print("Connection successful")
except Exception as e:
    print(f"Failed to connect: {e}")
