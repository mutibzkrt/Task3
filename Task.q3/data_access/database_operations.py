# data_access/database_operations.py
import sqlite3

class DatabaseOperations:
    def __init__(self, db_name="mydatabase.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Musteriler (
            MusteriID INTEGER PRIMARY KEY AUTOINCREMENT,
            Ad TEXT NOT NULL,
            Soyad TEXT NOT NULL,
            Email TEXT NOT NULL,
            Telefon TEXT NOT NULL,
            Adres TEXT
        );
        """)
        self.connection.commit()

    def insert_customer(self, ad, soyad, email, telefon, adres):
        self.cursor.execute("""
        INSERT INTO Musteriler (Ad, Soyad, Email, Telefon, Adres) 
        VALUES (?, ?, ?, ?, ?)
        """, (ad, soyad, email, telefon, adres))
        self.connection.commit()

    def update_customers(self):
        self.cursor.execute("""
        UPDATE Musteriler 
        SET Telefon = '555-999-0000' 
        WHERE MusteriID % 10 = 0
        """)
        self.connection.commit()

    def delete_customers(self):
        self.cursor.execute("""
        DELETE FROM Musteriler 
        WHERE MusteriID % 5 = 0
        """)
        self.connection.commit()

    def close(self):
        self.connection.close()
