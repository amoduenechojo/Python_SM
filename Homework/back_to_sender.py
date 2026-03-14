

deliveries = int(input("Enter your successful deliveries: "))

while (deliveries < 0 or deliveries > 100):
    print("Re-enter a valid input: ")
    deliveries = int(input("Enter your successful deliveries: "))

base_pay = 5000
amount_parcel = 0

if (deliveries < 50):
    amount_parcel = 160


elif(deliveries >= 50 and deliveries <= 59):
    amount_parcel = 200


elif(deliveries >= 60 and deliveries <= 69):
    amount_parcel = 250


elif (deliveries >= 70):
    amount_parcel = 500


else:
    print("Invalid delivery rate.")
    

wage_for_the_day = deliveries * amount_parcel + 5000
print("The riders wage is: " , wage_for_the_day)
