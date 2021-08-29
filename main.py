from admin import retrieve_data2
import sys
import csv
import user
import admin


while True:
    print('\n1. Enter Donor data\t2. Register Hospital/camps(admin) \n3. Retrieve Donor specific data \t4. Retrieve Recipient specific data\n5. Exit system')
    ch = int(input('\nSelect method :'))

    if ch == 1:
        user.userinput()
    elif ch == 2:
        admin.addCamp()
    elif ch == 3:
        admin.retrieve_data1()
    elif ch == 4:
        admin.retrieve_data2()
    elif ch == 5:
        print('\n\nThank you for using this system!\n\n')
        sys.exit(1)
    else:
        print("\n\nWrong Choice!! Try Again!!")