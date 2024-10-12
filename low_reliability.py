import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

def divide_numbers(a, b):
    return a / b  # No error handling for division by zero

def read_file(filename):
    file = open(filename, 'r')  # No error handling if file doesn't exist
    data = file.read()
    file.close()
    return data

def write_to_file(filename, data):
    file = open(filename, 'w')  # No error handling for permission issues
    file.write(data)
    file.close()

def calculate_average(numbers):
    return sum(numbers) / len(numbers)  # No handling for empty lists

def get_random_element(elements):
    return elements[random.randint(0, len(elements))]  # Off-by-one error

def main():
    print("Generated Password:", generate_password(8))

    num1, num2 = 10, 0
    print(f"Division Result: {divide_numbers(num1, num2)}")  # Will crash if num2 is 0

    filename = "nonexistent_file.txt"
    print(f"File Content: {read_file(filename)}")  # Will crash if file doesn't exist

    data = "Sample text"
    write_to_file("output.txt", data)  # May crash if write permissions are missing

    numbers = []
    print(f"Average: {calculate_average(numbers)}")  # Will crash on empty list

    elements = ["apple", "banana", "cherry"]
    print(f"Random Element: {get_random_element(elements)}")  # Off-by-one error

if __name__ == "__main__":
    main()
