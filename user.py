import csv
from datetime import date
# bloodgroup = ['a+','a-','b+','b-','o+','o-','ab+','ab-']

todaydate = date.today()

def userinput():
    print('\nEnter the following details:')
    name = input("Donor name:")

    city = input("\nCity:")
    phno = int(input("\nPhone Number:"))
    email = input("\nEmail id:")
    bg = input("\nBloodGroup")
    age = int(input("\nAge:"))
    with open('users.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([email, name, city, phno, bg, age, todaydate])
        f.close()
    print("\n\nThank You!!New Donor Registered")
