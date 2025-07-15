def reverse_string(input_string: str) -> str:

    if len(input_string) <= 1:
        return input_string
    else:
        return input_string[-1] + reverse_string(input_string[:-1])

if __name__ == "__main__":
    print(">>>>>>>>> Recursive Reverse String <<<<<<<<<")
    input_value = input("Enter the string to be reversed: ")
    print(reverse_string(input_value))