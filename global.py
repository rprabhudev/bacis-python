#gobal variable

a=10# 'a' globally declared
print("global a=",a)
print(id(a)) # id is used to print the memory address
def dummy1():
    print("in function",a)#a is global
dummy1()
def dummy2():
    a=15 #a is local
    print("in function",a)
dummy2()
def dummy3():
    global a#changing global variable inside function
    a=35
    print("in function",a)
dummy3()
def dummy4():
    a=9
    x=globals()['a']
    print("in function",a)
    print("assign global in local",x)
    print(id(x))
    globals()['a']=25# change the global variable leaving the local
   
dummy1()
dummy4()
print("outside",a)# a is global
