#vote

count_nanda = 0
count_kabil = 0
count_else = 0


while True:
    print('''
    press 1 to cast your vote for Nanda _/\_
    press 2 to cast your vote for kabil \m/
    press 3 to cast your vote for NOTA :-|
    press 4 to close Voting
    ''')
    option = int(input("Cast your Vote :   "))
    if option == 1:
        count_nanda +=1
    elif option == 2:
        count_kabil +=1
    elif option == 3:
        count_else +=1
    elif option ==4:
        break
    else:
        print("Wrong choise , you have not casted your vote")

print("------------------Result-------------------------")
print("\n")
print("No of vote for Nanda _/\_ :", count_nanda)
print("\n")
print("No of vote for Kabil \m/ :", count_kabil)
print("\n")
print("No of vote for NOTA :-|:", count_else)
if count_nanda == count_kabil and count_kabil==count_else and count_else==count_nanda:
    print("No one Elected")
elif count_nanda>count_kabil and count_nanda>count_else:
    print("_/\_officially elected ")
    #max = count_nanda
    print("maximum vote for _/\_")
    if count_kabil==count_else:
        #min = count_else
        print("minimum vote for :-|")
        print("minimum vote for \m/")
    elif count_kabil<count_else:
        #min = count_kabil
        print("minimum vote for \m/")
    else:
        print("minimum vote for :-| ")
        

elif count_kabil>count_nanda and count_kabil >count_else:
    print("\m/ officially elected")
    print("maximum vote for \m/")
    if count_nanda==count_else:
        print("minimum vote :-|")
        print("minimum vote _/\_")
    elif count_nanda<count_else:
        print("minimum vote _/\_")
    else:
        print("minimum vote :-| ")

elif count_else>count_kabil and count_else>count_nanda:
    print(":-| officialy elcted")
    print("maximum vote for :-|")
    if count_kabil==count_nanda:
        print("minimum vote _/\_")
        print("minimum vote for \m/")
    elif count_kabil<count_nanda:
        print("minimum vote for \m/")
    else:
        print("minimum vote _/\_")
        

else:
    print("no one elected")

