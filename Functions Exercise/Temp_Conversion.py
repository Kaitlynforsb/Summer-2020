# Kaitlyn Forsberg
# declare function that changes temp in Celsius to Fahrenheit
def temp_to_fahren(temp):
    return (temp * (9 / 5)) + 32


# declare function that changes temp in Fahrenheit to Celsius
def temp_to_celsius(temp):
    return (temp - 32) * (5 / 9)


choice = input("Would you like to convert a temperature to Fahrenheit from Celsius (F)" 
               " or to Celsius from Fahrenheit (C)? ")
# input is a string -> change to float
temperature = input("Please enter a temperature to be converted: ")
temperature = float(temperature)

if choice == "F":
    print(temp_to_fahren(temperature))
elif choice == "C":
    print(temp_to_celsius(temperature))
