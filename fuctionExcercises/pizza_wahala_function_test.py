from unittest import TestCase
import pizza_wahala_function


class PizzaWahalaFunctionTest(TestCase):

    def test_that_no_of_pizza_in_sapa_size_is_four(self):

        guests = 4
        slice_per_box = 4
        price_per_box = 2200

        boxes, leftover, cost = pizza_wahala_function.pizza_workings(guests, slice_per_box, price_per_box)
        self.assertEqual(boxes, 1)



    def test_that_no_of_pizza_in_sapa_size_is_six(self):

        guests = 2373
        slice_per_box = 6 
        price_per_box = 2400

         boxes, leftover, cost = pizza_wahala_function.pizza_workings(guests, slice_per_box, price_per_box)
        self.assertEqual(boxes, 1)


     def test_that_no_of_pizza_in_sapa_size_is_eight(self):

        guests = 274
        slice_per_box = 8
        price_per_box = 3000

         boxes, leftover, cost = pizza_wahala_function.pizza_workings(guests, slice_per_box, price_per_box)
        self.assertEqual(boxes, 1)


    
     def test_that_no_of_pizza_in_sapa_size_is_eight(self):

        guests = 27
        slice_per_box = 12
        price_per_box = 4200

         boxes, leftover, cost = pizza_wahala_function.pizza_workings(guests, slice_per_box, price_per_box)
        self.assertEqual(boxes, 1)


