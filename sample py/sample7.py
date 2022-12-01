
class Person:
    def __init__(self,name,age,location):
        self.name=name
        self.age=age
        self.location=location
    def data(self):
        print(self.name,"age is", self.age, "and location is", self.location)
    
s=Person("jeeva" ,21,"salem")

class work1(Person):
    def __init__(self, name, age, location):
        super().__init__(name, age, location)
x=work1("kalai",21,"chennai")

class work2(Person):
    def __init__(self, name, age, location):
        super().__init__(name, age, location)
y=work1("vasim",21,"bangalore")
             
s.data()
x.data()
y.data()   
