#method overriding
class A:
    def show(self):
        print("in A")

class B(A):
    def show(sel):
        print("in B")
class c(A):
    pass

a1 = B()#oject of b 
a2 = c()#object o c
a1.show()#b oject calling method of its own class
a2.show()#c oject calling method from super class 