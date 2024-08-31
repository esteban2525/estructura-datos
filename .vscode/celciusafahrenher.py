def celsius_a_fahrenheit(celsius):
   
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    
    celsius = (fahrenheit - 32) * 5/9
    return celsius

#uso
temperatura_celsius = 25
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")

temperatura_fahrenheit = 77
temperatura_celsius = fahrenheit_a_celsius(temperatura_fahrenheit)
print(f"{temperatura_fahrenheit}°F es igual a {temperatura_celsius}°C")