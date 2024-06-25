def hash_algorithm(input_string):
    current_value = 0

    for char in input_string:
        ascii_code = ord(char)  # Determine the ASCII code for the current character
        current_value += ascii_code  # Increase the current value by the ASCII code
        current_value *= 17  # Multiply the current value by 17
        current_value %= 256  # Set the current value to the remainder of dividing itself by 256

    return current_value

# Example usage:
input_string = "rn"
result = hash_algorithm(input_string)
print(f"The HASH value for '{input_string}' is: {result}")
