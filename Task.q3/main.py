# main.py
from business.customer_manager import CustomerManager
import time

def main():
    customer_manager = CustomerManager()
    
    print("100.000 kayıt ekleniyor...")
    start_time = time.time()
    customer_manager.add_customers()
    print(f"Kayıtlar eklendi. Süre: {time.time() - start_time:.2f} saniye")

    print("Kayıtlar güncelleniyor...")
    start_time = time.time()
    customer_manager.update_customers()
    print(f"Kayıtlar güncellendi. Süre: {time.time() - start_time:.2f} saniye")

    print("Kayıtlar siliniyor...")
    start_time = time.time()
    customer_manager.delete_customers()
    print(f"Kayıtlar silindi. Süre: {time.time() - start_time:.2f} saniye")

    customer_manager.close_connection()

if __name__ == "__main__":
    main()
