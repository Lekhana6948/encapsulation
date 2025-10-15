

class BankAccount:

      def __init__(self,owner,balance):
        self.owner = owner          #public
        self.__balance = balance    #private


      def bygetter(self):
        return self.__balance


      def bysetter(self,amount):
        if amount>=0;
          self.__balance = amount
          else:
            print("Invalid amount")

obj =BankAcount("Imran",2200)

print(obj.bygetter())

obj.bysettter(54000)
print(obj.bygetter())

