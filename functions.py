#function
def tennis():#function decaration
    print("roger")
    print("monfils") #function defenition
tennis() #funtion call

# parameterized function
def calc(a,b):
    c = a+b
    d = a-b
    return c,d #return statement
result1, result2 = calc(25,20) # function call get a value
print(result1, result2)

def add(a,b):# ormal arguments
    c=a+b
    print(c)

add(1,5)#actual arguement

def details1(name,age):
    print(name)
    print(age+10) #cannot do operations with string and int

#details1( 25, "abcd" )#position argument

def details2(name,age):
    print(name)
    print(age)

details2(age= 25, name="abcd" )#keyword argument


def details3(name,age=18):#default argument
    print(name)
    print(age)

details3("abcd " )#keyword argument
details3("qwerty",25)

def sum(a,*b):# *variable length arguments
    c=a
    for i in b:
        c +=i
    print(c)
sum(1,25,6,354) #variable length arguments

def details4(name,**data): #** variable keyword argument
    print(name)
    for i,j in data.items():
        print(i,j)
details4("roger", age=35, country="swiss", no=89863)



