
from oopsdemo import calculator

class childImp1(calculator):
     num2=  200

     def __init__(self):
         calculator.__init__(self, 3, 15)


     def getCompletedata(self):
         return self.num2+self.num+self.summation()


obj = childImp1()
print(obj.getCompletedata())






