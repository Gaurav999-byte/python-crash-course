class Student:

      def __init__(self,name,marks):
            self.name=name
            self.marks=marks

      @staticmethod
      def hello():
            print("hello")
      
      def get_avg(self):
            sum=0
            for ele in self.marks:
                  sum=sum+ele

            print("average score of",self.name," is",sum/3)

s1=Student("TEJAS",[61,68,92])
s1.get_avg()
s1.hello()

s1.name="iron"
s1.get_avg()