import csv
import python_connect
file = open('mydata.xlsx', 'w')
file = csv.writer(file)
file.writerow(['Name', 'Age', 'email', 'mobile number'])
n = int(input('How many records you want to insert: '))
for i in range(n):
    name = input(f'{i+1}. Enter name: ')
    age = input(f'{i+1}. Enter age: ')
    email = input(f'{i+1}. Enter your email: ')
    mobile = input(f'{i+1}. Enter Mobile number: ')
    file.writerow([name, age, email, mobile])
    print()
print('All records inserted successfully !')