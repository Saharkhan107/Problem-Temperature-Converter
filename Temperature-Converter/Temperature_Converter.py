# Temperature Converter
# Name: Sahar Iqbal
# Date: 10/19/2024

def convert_temperature(temperature, unit):
    if unit.upper() == 'C':
        # Convert Celsius to Fahrenheit
        converted = (temperature * 9/5) + 32
        return converted
    elif unit.upper() == 'F':
        # Convert Fahrenheit to Celsius
        converted = (temperature - 32) * 5/9
        return converted
    else:
        raise ValueError("Unit must be 'C' for Celsius or 'F' for Fahrenheit.")

# Example usage
try:
    print(convert_temperature(32, 'F'))  # Output: 0.0
    print(convert_temperature(0, 'C'))   # Output: 32.0
    print(convert_temperature(100, 'C')) # Output: 212.0
    print(convert_temperature(212, 'F')) # Output: 100.0
except ValueError as e:
    print(e)

