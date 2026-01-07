print("Good day,Welcome to Iya Scambirah Pizza Joint!")

pizza_types = {
    "sapa": {"slices":4 ,  "price": 2200},
    "Small money": {"slices":6 ,  "price": 2400},
    "Big boys": {"slices":8 ,  "price": 3000},
    "Odogwu": {"slices":12 , "price": 4200},
    }

guests = int(input("Number of guests: "))
pizza_choice = (input("Choose pizza type(sapa, small money, big boys, odogwu): "))

slice_per_box = pizza_types[pizza_choice]["slices"]
price_per_box = pizza_types[pizza_choice]["price"]

boxes = guests // slice_per_box
if guests % slice_per_box != 0:
    boxes = boxes + 1

total_slices = boxes * slice_per_box
leftover_slices = total_slices - guests

total_cost = boxes * price_per_box

print("Boxes needed: " , boxes)
print("Slices leftover: " ,  leftover_slices)
#print("Slices leftover: " ,  leftover_slices)
print("Total amount to pay: " , total_cost)


   

