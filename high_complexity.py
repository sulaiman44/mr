def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def calculate_factorial(n):
    """Calculate factorial recursively with error handling."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def process_numbers(numbers):
    """Process a list of numbers with multiple conditions and loops."""
    results = []
    for num in numbers:
        if num % 2 == 0:
            if num % 5 == 0:
                results.append(f"{num} is divisible by 10")
            else:
                results.append(f"{num} is even but not divisible by 5")
        elif num > 10:
            results.append(f"{num} is odd and greater than 10")
        else:
            results.append(f"{num} is odd and less than or equal to 10")
    
    return results

def fibonacci(n):
    """Generate Fibonacci sequence up to n."""
    sequence = [0, 1]
    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

def find_max_min(numbers):
    """Find both the maximum and minimum in a list of numbers."""
    if not numbers:
        return None, None
    max_num = numbers[0]
    min_num = numbers[0]
    
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num

def complex_function(a, b, c):
    """A complex function with nested conditionals and multiple branches."""
    if a > 10:
        if b < 5:
            if c % 2 == 0:
                return "Branch 1: a > 10, b < 5, c is even"
            else:
                return "Branch 2: a > 10, b < 5, c is odd"
        else:
            return "Branch 3: a > 10, b >= 5"
    elif a < 0:
        return "Branch 4: a is negative"
    else:
        if c == 0:
            return "Branch 5: a between 0 and 10, c is zero"
        else:
            return "Branch 6: a between 0 and 10, c is non-zero"

def main():
    # Palindrome check
    word = "racecar"
    print(f"Is '{word}' a palindrome? {is_palindrome(word)}")

    # Factorial calculation
    n = 5
    print(f"Factorial of {n}: {calculate_factorial(n)}")

    # Process a list of numbers
    numbers = [3, 10, 15, 20, 25]
    print("Number processing results:")
    for result in process_numbers(numbers):
        print(result)

    # Fibonacci sequence
    fibonacci_limit = 10
    print(f"Fibonacci sequence up to {fibonacci_limit}: {fibonacci(fibonacci_limit)}")

    # Max and Min in a list
    print(f"Max and Min in the list {numbers}: {find_max_min(numbers)}")

    # Complex branching function
    print(f"Complex function result: {complex_function(12, 3, 4)}")
    print(f"Complex function result: {complex_function(8, 10, 0)}")

if __name__ == "__main__":
    main()
