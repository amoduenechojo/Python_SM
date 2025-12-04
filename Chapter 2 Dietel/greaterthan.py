num_1 = int(input("Enter first integer: "))
num_2 = int(input("Enter second integer: "))
num_3 = int(input("Enter third integer: "))

if(num_1 <= num_2 <= num_3):

    print("numbers in ascending order:", num_1, num_2, num_3)
else:
    print("num_1, num_3, num_2")

else if ("num_2 <= num_1 <= num_3"):
   print("numbers in ascending order: ", num_2, num_1, num_3)
else: 
    print("num_1 , num_3 , num_1")
