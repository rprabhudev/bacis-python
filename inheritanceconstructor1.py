class A:#super class
    def __init__(self) -> None:#constructor of class a
        print("init in a")
    def method1(self):
        print("method 1 running")
    def method2(self):
        print("method2 running")

class B(A):#sub class or child class
    def __init__(self) -> None:#constructor of class b
        super().__init__()# super keyword to point constructor of superclass
        print("in init b")
    def method3(self):
        print("method 3 running")
    def method4(self):
        print("method4 running")
class C:
    def __init__(self) -> None:
        print("init in c")
    
class D:
    def __init__(self) -> None:
        print("init in d")
  
class E(C,D):
    
    def __init__(self) -> None:
        super().__init__()
        print("init in e")
   
b1 = B()
e1 = E()