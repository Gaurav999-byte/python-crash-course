class Student:
      college_name="abc college" #class attribute
      def __init__(self,name,marks): #parametise constructr
            self.name=name #object attribute
            self.marks=marks
            print("adding new student in database")



s1=Student("karan",90) #attributes
print(s1.name,s1.marks,s1.college_name)

s2=Student("arjun",95)
print(s2.name,s2.marks,s1.college_name)

# class attribute < object attribute