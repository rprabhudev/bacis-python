students ={}
while True:
    try:
        print('''
    press 1 to creating new student
    press 2 to view student
    press 3 to update student
    press 4 to delete student 
    press 5 to exit
        ''')
        option =int(input("Enter option : "))
        if option == 1:
            id = int(input("Enter student ID : "))
            name = input("Enter student name : ")
            age = int(input("Enter student age : "))
            dept = input("Enter student Department : ")
            students[id]={
                "Name" : name,
                "Age" : age,
                "Department" : dept
            }
            print("Student profile created")
        
        elif option==2:
            data = int(input("Enter student ID : "))
            print("Student ID {}".format(data))
            #print(students[data].name)
            for x,y in students[data].items():
                print(x,y)
        
        elif option == 3:
            data = int(input("Enter student ID : "))
            print("Student {}".format(data))
            name = input("Enter student name : ")
            age = int(input("Enter student age : "))
            dept = input("Enter student Department : ")
            students[data]={
                "Name" : name,
                "Age" : age,
                "Department" : dept
            }
            print("Student profile updated")
        elif option == 4:
            data = int(input("Enter student ID : "))
            print("Student ID {}".format(data))
            del students[data]
            print("Student profile deleted")

        elif option == 5:
            break

        else:
            print("wrong choise")
    except Exception as e:
        print(e)
    

        
