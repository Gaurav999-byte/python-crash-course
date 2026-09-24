class Account:
      def __init__(self,bal,acn):
            self.bal=bal
            self.acn=acn

      def debit(self,amt):
            self.bal=self.bal-amt
            print("Rs.",amt,"was debited")
            print("curr balance",self.get_balance())


      def credit(self,amt):
            self.bal=self.bal+amt
            print("Rs.",amt,"was credited")
            print("curr balance",self.get_balance())
            


      def get_balance(self):
            return self.bal

ac1=Account(500000,12345)
ac1.debit(20)
ac1.credit(10)