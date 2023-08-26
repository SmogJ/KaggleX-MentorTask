# main out put for the code
def main():
    temp= degree()
    print(f"{convert_temperature(temp)}F")

# Getting input from user and formatting from string to integer    
def degree():
    # using try except to catch error and wrong input from user, and request for the rigth input
    try:
        celsius= int(input('Enter your Tempature in Celsius: ').strip('Cc'))
        return celsius
    except ValueError:
        print("\nInvalid Input. Please enter a number like 35C, 35 C or 35c, 35 c")
        return degree()
    
# Convert the integer to Fehrenheit
def convert_temperature(celsuis):
    Fahrenheit= (celsuis  * (9/5)) + 32 # using a mathamatical formular to convert to Fahrenheit   
    return Fahrenheit

    
main()