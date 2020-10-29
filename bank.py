#bank

account = {}
print("Welcome to Banking service......__/\_ ")
while True:
    print('''
    BANKING
    Press 1 to add New Account
    Press 2 to add Amount
    Press 3 to Withdarw Amount
    Press 4 to Print Account Details
    Press 5 to Close the account
    Press 6 to Exit     
    ''')
    option = int(input("Please enter the choise"))
    if option == 1:
        code = input("Enter bank code : ")
        name = input("Enter name : ")
        pin = int(input("Enter PIN : "))
        intial = int(input("Enter amonut for intial creation minimum1000 : "))
        account[pin] = {
            "Code" : code,
            "Name" :name,
            #"PIN" = pin,
            "Balance" : intial
        }
        print("Account Created Successully")
        for key, value in account[pin].items():
            print(key , '----->', value)
    elif option == 2:
        pin = int(input("Enter PIN"))
        amount = int(input("Enter amount to be added"))
        code = account[pin].get("Code")
        name = account[pin].get("Name")
        available = account[pin].get("Balance")
        account[pin]={
            "Code" : code,
            "Name" :name,
            "Balance" : available+amount
        }
        for key, value in account[pin].items():
            print(key , '----->', value)

    elif option == 3:
        pin = int(input("Enter PIN"))
        amount = int(input("Enter amount to Withdraw"))
        code = account[pin].get("Code")
        name = account[pin].get("Name")
        available = account[pin].get("Balance")
        account[pin]={
            "Code" : code,
            "Name" : name,
            "Balance" : available-amount
        }
        for key, value in account[pin].items():
            print(key , '----->', value)
    elif option == 4:
        pin = int(input("Enter PIN : "))
        for key, value in account[pin].items():
            print(key , '----->', value)
        
    elif option == 5:
        data = int(input("Enter PIN to Close the Account : "))
        del account[data]
        print("Acconut closed sucefully")
      
    elif option == 6:
        break
    else :
        print("Wrong choise")


