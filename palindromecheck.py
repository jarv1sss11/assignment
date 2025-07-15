def is_palindrome(s):
    stack = []

    for char in s:
        stack.append(char)


    reversed_s = ""
    while stack:
        reversed_s += stack.pop()


    if s == reversed_s:
        print(f'"{s}" is a palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')

is_palindrome("did")
is_palindrome("feed")