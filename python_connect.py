import mysql.connector
import xlrd

conn = mysql.connector.connect(host='localhost',username='root',password='asim',database='student')
my_cursor=conn.cursor()

my_cursor.execute("create table asim(name varchar(30), age int, email varchar(30), mobile long)")

loc=("C:\\Users\\samsung\\Desktop\\data.xlsx")

l=list()
a=xlrd.open_workbook(loc)
sheet=a.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(1,3):
    l.append(tuple(sheet.row_values(i)))
# # conn.commit()

q="insert into asim(name, age, email, mobile)values(%s,%s,%s,%s)"
my_cursor.executemany(q,l)
conn.commit()
conn.close()
# print("Connection succesfully created!")