def checker(number):
    if isinstance(number, (int, float)):
        if number % 2 == 0:
            print("The number is even")
        else:
            print("The number is odd")
    else:
        print("Input is not a number")