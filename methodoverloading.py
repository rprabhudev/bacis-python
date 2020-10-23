#method overloading
class student:
           
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
s1 = student()
print(s1.sum(90,50))
print(s1.sum(90,))
print(s1.sum(90,50,60))