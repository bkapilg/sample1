#self keyword is mandatory for calling variable name into method
#instance and class variable have whole different purpose
#constructor name should be ____init_
#new keyword is not required when you create object

class calculator:
     num = 100

     #default constructer

     def __init__(self,a,b):
         self.firstNumber= a
         self.secondNumber= b
         print("i am called automatically when object is created")

     def getdata(self):
         print("i am now executing as method in class")

     def summation(self):
        return self.firstNumber + self.secondNumber + calculator.num

obj=calculator(2,3) #syntax to create a class in python
obj.getdata()
print(obj.summation())

obj1=calculator(4, 5)
obj1.getdata()
print(obj1.summation())


