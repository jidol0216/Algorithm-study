import pymysql

conn = pymysql.connect(
    host ="localhost",
    user="root",
    password="1234",
    database="exampledb",
   
)
cursor = conn.cursor()

sql1="""
INSERT INTO users (name, age, email) VALUES ('Alice', 25, 
'alice@example.com');

"""

sql="""
INSERT INTO users (name, age, email) VALUES (%s,%s,%s);

"""

cursor.execute(sql1)
cursor.execute(sql,('Charlie',32,'charlie@gmail.com'))
conn.commit()
print("data insert complete")

conn.close()