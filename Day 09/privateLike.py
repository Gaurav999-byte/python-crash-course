class Amount:
      def __init__(self,accno,accnpass):
            self.accno=accno
            self.__accnpass=accnpass


      def reset(self):
            print(self.__accnpass)


s=Amount("1234","@abc567")

print(s.accno)
s.reset()
            