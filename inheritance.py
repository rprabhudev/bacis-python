class A:#super class
    def method1(self):
        print("method 1 running")
    def method2(self):
        print("method2 running")
#single inheritance
class B(A):#sub class or child class
    def method3(self):
        print("method 3 running")
    def method4(self):
        print("method4 running")
#multi level inheritance
class C(B):
    def method5(self):
        print("method 5 working")
class D():
    def method6(self):
        print("method 6 working")
#multiple inheritance
class E(A,D):
    def method7(self):
        print("method 7 working")


a1 = A()
a1.method1()
a1.method2()
b1 = B()
b1.method2()#class b object using class Amethod 
b1.method1()
c1 = C()
c1.method1()#class c inheriting methods of class Aand B
e1 = E()
#class e object inheriting methods of class A and D
e1.method1()
e1.method2()
e1.method6()
e1.method7()
