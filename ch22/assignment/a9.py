from openpyxl import Workbook


wb = Workbook()

ws = wb.active
ws.title = "Sheet1"

wb.save(r"C:/rokey/python/ch22/assignment/data.xlsx")

print("data.xlsx 파일이 생성되었습니다.")
