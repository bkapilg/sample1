number=input("enter the  num")
number=int(number)
if(number==0):
    print("num is zero ")
elif(number>0):
    print("number is positive number")
    if(number%2==0):
     print("number is even number")
    else:
     print("number is odd number")
else:
    print("number is negative number")
