class Student:
      
      def __init__(self,name,marks): #parametise constructr
            self.name=name #object attribute
            self.marks=marks
           
      def welcome(self):
            print("welcome student",self.name)

      def get_marks(self):
            return self.marks


s1=Student("Gaurav",100)
s1.welcome()
print(s1.get_marks())
