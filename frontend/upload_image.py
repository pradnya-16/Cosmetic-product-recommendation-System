import cgi
import mysql.connector
from mysql.connector import Error

# Connect to MySQL database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )
    cursor = conn.cursor()
except Error as e:
    print("Error connecting to MySQL database:", e)
    exit()

# Process uploaded image
form = cgi.FieldStorage()
if "image" in form:
    image_file = form["image"]
    image_data = image_file.file.read()
    image_name = image_file.filename

    # Insert image data into database
    try:
        query = "INSERT INTO images (name, data) VALUES (%s, %s)"
        cursor.execute(query, (image_name, image_data))
        conn.commit()
    except Error as e:
        print("Error inserting image data into database:", e)
        conn.rollback()

# Close database connection
cursor.close()
conn.close()
