# business/customer_manager.py
from data_access.database_operations import DatabaseOperations

class CustomerManager:
    def __init__(self):
        self.db_operations = DatabaseOperations()

    def add_customers(self, count=100000):
        for i in range(count):
            ad = f"Ad{i}"
            soyad = f"Soyad{i}"
            email = f"email{i}@example.com"
            telefon = f"555-000-{i:04d}"
            adres = f"Adres{i}"
            self.db_operations.insert_customer(ad, soyad, email, telefon, adres)

    def update_customers(self):
        self.db_operations.update_customers()

    def delete_customers(self):
        self.db_operations.delete_customers()

    def close_connection(self):
        self.db_operations.close()
