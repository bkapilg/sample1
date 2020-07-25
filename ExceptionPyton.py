
ItemsInCart = 0
#2 item will be added to the cart

if(ItemsInCart!=2):   #raise Exception("product cart count not matching")
     assert(ItemsInCart==0)

#try ,catch

try:
    with open('text.txt', 'r') as reader:
        reader.read()

except Exception as e:
    #print("some has i reached this block because there is failure in try block")
    print(e)
finally:
     print("cleaning up resources")