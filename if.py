#conditional statement
print("if statement")

a = int(input("enter a number"))
b = int(input(" enter a number"))
print("greatest of two numbers")
if a>b:
    print(" if condtion is true a greatest")
    
else:
    print("else condition b greates")
c = int(input(" enter a number"))
print("greatest of three numbers")
if a > b:
    if a>c:
        print("if condtion true")
        print("nestedif true a greatest")
    elif b>c:
        print("elif true b greatest")
else:
    print("else true c greatest")

#short hand if
if a>b : print("a")

#short hand if else
print("a") if a>b else print("b")

#short hand ternary operator
print("a") if a>b else print("=") if a==b else print("b")

#And

if a>b and b>c :
    print("both true")

#or
if a>b or b>c :
    print("atlest one condition is true") 
        
