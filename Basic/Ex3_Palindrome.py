#Question: Write a function to check if a given string is a palindrome.

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
