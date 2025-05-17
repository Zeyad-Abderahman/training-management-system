import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="P@ss01281",  # ✅ use this new password
        database="training_mm"
    )
