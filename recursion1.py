
def multiply_by_adding(r: int, s: int) -> int:
    r = abs(r)
    s = abs(s)
    if s == 0:
        return 0
    elif s == 1:
        return r
    else:
        return r + multiply_by_adding(r, s - 1)

print(">>>>>> Multiply by Adding <<<<<<")

r = int(input("Enter the first number: "))
s = int(input("Enter the second number: "))

sign = -1 if (r < 0) ^ (s < 0) else 1


result = sign * multiply_by_adding(r, s)


print(f"Result: {result}")