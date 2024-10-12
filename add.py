import math

def calculate_area_of_circle(radius):
    if radius < 0:
        return "Radius cannot be negative"
    return math.pi * (radius ** 2)

def calculate_perimeter_of_circle(radius):
    if radius < 0:
        return "Radius cannot be negative"
    return 2 * math.pi * radius

def find_maximum(numbers):
    if len(numbers) == 0:
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

def find_minimum(numbers):
    if len(numbers) == 0:
        return None
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

def convert_temperature(temp, scale):
    if scale not in ["C", "F"]:
        return "Invalid scale"
    if scale == "C":
        return (temp * 9/5) + 32  # Celsius to Fahrenheit
    elif scale == "F":
        return (temp - 32) * 5/9  # Fahrenheit to Celsius

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0:
        return 1
    return n * factorial(n - 1)

def print_prime_numbers_up_to(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    print("Prime numbers:", primes)

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    return result

# Example usage
if __name__ == "__main__":
    print("Area of circle with radius 5:", calculate_area_of_circle(5))
    print("Perimeter of circle with radius 5:", calculate_perimeter_of_circle(5))

    numbers = [3, 1, 4, 1, 5, 9, 2]
    print("Maximum:", find_maximum(numbers))
    print("Minimum:", find_minimum(numbers))

    print("Convert 100 Celsius to Fahrenheit:", convert_temperature(100, "C"))
    print("Convert 32 Fahrenheit to Celsius:", convert_temperature(32, "F"))

    print("Is 7 prime?", is_prime(7))
    print_prime_numbers_up_to(20)

    print("Factorial of 5:", factorial(5))

    print("10 divided by 2:", divide_numbers(10, 2))
    print("10 divided by 0:", divide_numbers(10, 0))
