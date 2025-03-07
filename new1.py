# import mysql.connector

# # Connect to MySQL
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="vglug@123",
#     database="Sample"
# )

# cursor = conn.cursor()

# # Retrieve data
# cursor.execute("SELECT * FROM SAMPLE")  # Replace 'users' with your table name
# rows = cursor.fetchall()

# # Display results
# for row in rows:
#     print(row)

# # Close connection
# cursor.close()
# conn.close()


n=int(input("enter a number:"))
if n%2==0:
    print("even")
else:
    print("odd")