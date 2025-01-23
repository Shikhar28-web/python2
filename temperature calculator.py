class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

def menu():
    converter = TemperatureConverter()

    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter choice (1/2): ")

    if choice in ['1', '2']:
        temp = float(input("Enter temperature: "))

        if choice == '1':
            converted_temp = converter.celsius_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp}°F")

        elif choice == '2':
            converted_temp = converter.fahrenheit_to_celsius(temp)
            print(f"{temp}°F is {converted_temp}°C")
    else:
        print("Invalid input!")

menu()
