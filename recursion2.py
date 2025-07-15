def check_if_prime_recursion(num, x):
    if x == 1:
        print("The number entered is prime!")
    elif num % x == 0:
        print(f"The number entered is divisible by: {x}")
        print("The number is not prime!")
        return
    else:
        check_if_prime_recursion(num, x - 1)

def check_if_prime(num: int):
    if num <= 1:
        print("Numbers less than or equal to 1 are not prime.")
    else:
        check_if_prime_recursion(num, num - 1)

if __name__ == "__main__":
    print(">>>>>>>> Test for Prime <<<<<<<<")
    try:
        number = int(input("Enter an integer to check: "))
        check_if_prime(number)
    except ValueError:
        print("Please enter a valid integer.")