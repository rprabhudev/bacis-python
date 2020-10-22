class student:#class declaration
    def __init__(self, name, rollno):#method declaration (constructor)
        self.name=name
        self.rollno=rollno
        self.lap = self.laptop()#object for inner class 
    
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
   
    class laptop:#class inside a class -inner class
       
        def __init__(self) -> None:
            self.brand = 'hp'
            self.ram = 5
        
        def show(self):
            print(self.brand,self.ram)

s1 = student('abcd',35)#object creation
s1.show()# function call
lap1 = s1.lap
lap2 = s2.lap
print(id(lap1))
print(id(lap2))
#print(s1.name,s1.rollno)

   