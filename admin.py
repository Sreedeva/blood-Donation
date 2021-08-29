import csv, sys
from datetime import date
import user

todaydate = date.today()
donor = []
reciepent = []

def addCamp():
    print('\n1. Enter passwrod to login as admin \t2. Exit')
    ch = int(input('\nSelect method :'))
    while True:
        if ch == 1:
            password = input('\nEnter Password :')
            if (password == "admin@123"):
                print('\nEnter the following details:')
                name = input("Enter Camp name:")
                city = input("\nCity:")
                phno = input("\nPhone Number:")
                email = input("\nEmail id:")
                address = input("\nAddress:")
                with open('camps.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([email, name, city, phno, address, todaydate])
                    f.close()
                print("\n\nThank You!!Your hospital/camp is Registered")
                sys.exit(1)
            else:
                print("Wrong Password")
                addCamp()
        if ch == 2:
            print('\n\nThank you for using this system!\n\n')
            sys.exit(1)


def retrieve_data1():
    print('\n1. Enter passwrod to login as admin \t2. Exit')
    ch = int(input('\nSelect method :'))
    while True:
        if ch == 1:
            password = input('\nEnter Password :')
            if (password == "admin@123"):
                with open('users.csv', 'r') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        donor.append(row)
                    uid = input('\nemail id:')
                    col = [x[0]for x in donor]
                if uid in col:
                    for x in range(0, len(donor)):
                        if uid == donor[x][0]:
                            print(donor[x])

                else:
                    print("\nInvalid ID!!")
                    f.close()
            else:
                print("Wrong Password")
                retrieve_data1()
        if ch == 2:
            print('\n\nThank you for using this system!\n\n')
            sys.exit(1)


def retrieve_data2():
    print('\n1. Enter passwrod to login as admin \t2. Exit')
    ch = int(input('\nSelect method :'))
    while True:
        if ch == 1:
            password = input('\nEnter Password :')
            if (password == "admin@123"):
                with open('camps.csv', 'r') as R:
                    reader = csv.reader(R)
                    for row in reader:
                        reciepent.append(row)
                Rid = input('\nemail id:')
                col = [x[0]for x in reciepent]
                if Rid in col:
                    for x in range(0, len(reciepent)):
                        if Rid == reciepent[x][0]:
                            print(reciepent[x])
                else:
                    print('\nInvalid ID')
                R.close()

            else:
                print("Wrong Password")
                retrieve_data2()
        if ch == 2:
            print('\n\nThank you for using this system!\n\n')
            sys.exit(1)
    
    
