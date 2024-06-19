import openpyxl
from openpyxl import Workbook
import random

# 제품 데이터 생성
product_ids = [f"P{str(i).zfill(3)}" for i in range(1, 101)]
product_names = [f"Product {i}" for i in range(1, 101)]
quantities = [random.randint(1, 100) for _ in range(100)]
prices = [round(random.uniform(10.0, 1000.0), 2) for _ in range(100)]

# 엑셀 파일 생성
wb = Workbook()
ws = wb.active
ws.title = "Products"

# 헤더 추가
ws.append(["제품ID", "제품명", "수량", "가격"])

# 데이터 추가
for i in range(100):
    ws.append([product_ids[i], product_names[i], quantities[i], prices[i]])

# 파일 저장
wb.save("products.xlsx")
