#bank
#import datetime
account = {}
bank = {}
print("Welcome to Banking service......__/\_ ")
while True:
    print('''
    BANKING
    Press 1 to add New Account
    Press 2 to add Amount
    Press 3 to Withdarw Amount
    Press 4 to Print Account Details
    Press 5 to Close the account
    Press 6 to List the accounts  
    Press 7 to Exit
    ''')
    option = int(input("Please enter the choise"))
    if option == 1:
        code = input("Enter bank code : ")
        name = input("Enter name : ")
        pin = int(input("Enter PIN : "))
        intial = int(input("Enter amonut for intial creation minimum1000 : "))
        account[name] = {
            "Code" : code,
            "Name" : name,
            "PIN" : pin,
            "Balance" : intial
        }
        #print(account)
        #bank[len(bank)]={"Code": code , "Name" : name ,"Balance" : intial }
        #print(account)
        print("Account Created Successully")
        for key, value in account[name].items():
            print(key , '----->', value)
    elif option == 2:
        data = input("Enter Name : ")
        mpin = int(input("Enter PIN for transaction"))
        tpin = account[data].get("PIN")
        if mpin == tpin:
                   
            amount = int(input("Enter amount to be added"))
            code = account[data].get("Code")            
            available = account[data].get("Balance")
            newbalance = amount+available
            #account["balance"] = newbalance
            account[data]={
                "Code" : code,
                "Name" :data,
                "Balance" : available+amount
            }
            for key, value in account[data].items():
                print(key , '----->', value)
        else:
            print("Wrong PIN")
        #bank[len(bank)]={"Code": account[data].get("Code") , "Name" : account[data].get("Name") ,"Balance" : account[data].get("Balance") }

    elif option == 3:
        data = input("Enter Name : ")
        mpin = int(input("Enter PIN for transaction : "))
        tpin = account[data].get("PIN")
        if mpin == tpin:
            amount = int(input("Enter amount to Withdraw"))
            code = account[data].get("Code")
            #name = account[pin].get("Name")
            available = account[data].get("Balance")
            newbalance = amount-available
            #account["balance"] = newbalance
            account[data]={
                "Code" : code,
                "Name" : data,
                "Balance" : available-amount
            }
            for key, value in account[data].items():
                print(key , '----->', value)
        else:
            print("Wrong PIN")
                
        #bank[len(bank)]={"Code": account[data].get("Code") , "Name" : account[data].get("Name") ,"Balance" : account[data].get("Balance") }
    elif option == 4:
        data = input("Enter Name : ")
        for key, value in account[data].items():
            print(key , '----->', value)
        
    elif option == 5:
        data = input("Enter Name : ")
        mpin = int(input("Enter PIN for transaction : "))
        tpin = account[data].get("PIN")
        if mpin == tpin:
            del account[data]
            print("Acconut closed sucefully")
        else:
            print("Wrong PIN")
                
        

    elif option == 6:
        #bank[len(bank)]={"Code": account.get("Code") , "Name" : account.get("Name") ,"Balance" : account.get("Balance") }
        result = bool(account)
        if result == True:
            for x ,y in account.items():
                print(x,"------->",y)
        else:
            print("no account list")
      
    elif option == 7:
        break
    else :
        print("Wrong choise")


