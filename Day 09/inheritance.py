class Car:
      @staticmethod
      def start():
            print("car started..")

      @staticmethod
      def stop():
            print("car stopped..")

class ToyotaCar(Car):
      def __init__(self,name):
            self.name=name

c1= ToyotaCar("frtuner")
c2=ToyotaCar("peius")

print(c1.start())