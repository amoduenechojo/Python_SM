formula = 0
temperature_converter = 0
celcius = 0

def temperature_converter(celcius):
    for number in range(0,6):
        if(temperature_converter <= -273):

            formula = (temperature_converter * 9/5) + 32
            temperature_converter += number

    print("Temperature in celcius: " , temperature_converter)
    print(formula)
       
    return formula







def calculating_factorial(number):
    multiplier = number - 1
