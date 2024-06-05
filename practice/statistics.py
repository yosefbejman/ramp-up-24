def analyze_numbers(numbers):
    if not numbers:
        print("The list is empty")
        return

    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = total / len(numbers)
    
    print(f"Sum: {total}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Average: {average}")
