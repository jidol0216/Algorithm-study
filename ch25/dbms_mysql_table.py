import pymysql

conn = pymysql.connect(
    host ="localhost",
    user="root",
    password="1234",
    database="exampledb",
   
)
cursor = conn.cursor()

sql="""
CREATE TABLE IF NOT EXISTS users (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
age INT,
email VARCHAR(100) UNIQUE
)




"""

cursor.execute(sql)
print("태이블 생성 완료")

conn.close()