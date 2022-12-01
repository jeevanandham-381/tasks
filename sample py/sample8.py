e#multiple inheritance
class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
class Father:
    fathername=""
    def father(self):
        print(self.fathername) 
class Son(Mother,Father):
    def parents(self):
         print("father is:" + self.fathername ,"mother is:" + self.mothername)
s=Son()
s.fathername="mahadevan"
s.mothername="tamilselvi"
s.parents()        

