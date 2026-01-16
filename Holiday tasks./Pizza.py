pizza_type = """
                S/N       PIZZA TYPE           SLICE/BOX      PRICE
                1:        Sapa size             4             2200
                2:        Small money size      6             2400
                3:        Big boys size         8             3000
                4:        Odogwu size           12            4200
"""
                
print(pizza_type)

#pizza_types_option = int(input("Enter a pizza type: "))

def pizza_workings(guests, slice_per_box, price_per_box):
            boxes = guests // slice_per_box
            if guests % slice_per_box != 0:
                boxes = boxes + 1
            print("The number of boxes needed is: " , boxes)

            total_slices = boxes * slice_per_box
            leftover_slices = total_slices - guests
            print("The leftover slices are: " ,  leftover_slices)

            total_cost = boxes * price_per_box
            print("The total cost is: ", total_cost)


pizza_type_option = int(input("Enter a pizza type: "))
guests = int(input("Enter number of guests: "))
   

match (pizza_type_option):
    case 1:
        slice_per_box = 4
        price_per_box = 2200
        pizza_workings(guests, slice_per_box, price_per_box)
    

    case 2: 
           slice_per_box = 6
           price_per_box : 2400
           pizza_workings(guests, slice_per_box, price_per_box)
        

    case 3: 
            slice_per_box = 8 
            price_per_box = 3000
            pizza_workings(guests, slice_per_box, price_per_box)
          

    case 4:
            slice_per_box = 8 
            price_per_box = 3000
            pizza_workings(guests, slice_per_box, price_per_box)
        

