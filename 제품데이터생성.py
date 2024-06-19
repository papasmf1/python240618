import sqlite3
import random

class ElectronicsDatabase:
    def __init__(self, db_name='electronics.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY,
                product_name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.connection.commit()
    
    def insert_product(self, product_id, product_name, price):
        self.cursor.execute('''
            INSERT INTO products (product_id, product_name, price)
            VALUES (?, ?, ?)
        ''', (product_id, product_name, price))
        self.connection.commit()
    
    def update_product(self, product_id, product_name=None, price=None):
        if product_name is not None:
            self.cursor.execute('''
                UPDATE products
                SET product_name = ?
                WHERE product_id = ?
            ''', (product_name, product_id))
        
        if price is not None:
            self.cursor.execute('''
                UPDATE products
                SET price = ?
                WHERE product_id = ?
            ''', (price, product_id))
        
        self.connection.commit()
    
    def delete_product(self, product_id):
        self.cursor.execute('''
            DELETE FROM products
            WHERE product_id = ?
        ''', (product_id,))
        self.connection.commit()
    
    def select_product(self, product_id):
        self.cursor.execute('''
            SELECT * FROM products
            WHERE product_id = ?
        ''', (product_id,))
        return self.cursor.fetchone()
    
    def select_all_products(self):
        self.cursor.execute('''
            SELECT * FROM products
        ''')
        return self.cursor.fetchall()
    
    def close(self):
        self.connection.close()

# 샘플 데이터 생성
def generate_sample_data(db):
    product_names = [f'Product {i}' for i in range(1, 101)]
    for i, name in enumerate(product_names, start=1):
        price = round(random.uniform(10.0, 1000.0), 2)
        db.insert_product(i, name, price)

# 데이터베이스 생성 및 샘플 데이터 삽입
db = ElectronicsDatabase()
generate_sample_data(db)

# 모든 제품 출력
all_products = db.select_all_products()
for product in all_products:
    print(product)

db.close()
