#exception
#a = int(input("enter a number"))
#b = int(input("enter a number"))
a=5
b=3
try:
    print("db open")
    print(a/b)
    #c =int('p')
except Exception as e:
    print(e)

finally:
    print("db closed")    