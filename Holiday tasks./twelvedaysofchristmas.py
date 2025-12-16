def day_names(day):
    days = ("first","second","third", "fourth", "fifth", "sixth", "seventh","eigth", "ninth", "tenth", "eleventh", "twelfth")
    return days[day-1]

def print_lyrics():
   gifts = (
    "A partridge in a pear tree.",
    "Two turtle doves, and",
    "Three french hens,"
    "Four calling birds,"
    "Five golden rings,"
    "Six geese a laying,"
    "Seven swams a swimming,"
    "Eight made a-milking,"
    "Nine ladies dancing,"
    "Ten lords a-leaping,"
    "Eleven pipers piping,"
    "Twelve drummers drumming."
)

for days in range(1,13):
    print(f" on the {day_names(days)} day of Christmas, my true love sent to me: ")
    for gifts in reversed(gifts[:day]):
        print(gifts)
    print()
