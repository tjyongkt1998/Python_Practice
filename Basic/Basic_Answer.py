def reverse_string(s: str) -> str:
    return s[::-1]

print(reverse_string("hello"))  # Output: "olleh"

#--------------------------------------------------------------
def find_max(lst: list) -> int:
    return max(lst)

print(find_max([3, 5, 1, 2, 4]))  # Output: 5



#--------------------------------------------------------------
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False



#--------------------------------------------------------------

def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz()


#--------------------------------------------------------------

def merge_sorted_lists(lst1: list, lst2: list) -> list:
    return sorted(lst1 + lst2)

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]


#--------------------------------------------------------------

def second_largest(lst: list) -> int:
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2]

print(second_largest([3, 5, 1, 2, 4]))  # Output: 4


#--------------------------------------------------------------

def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))    # Output: False


#--------------------------------------------------------------

def count_occurrences(s: str, char: str) -> int:
    return s.count(char)

print(count_occurrences("hello world", "o"))  # Output: 2


#--------------------------------------------------------------

def intersection(lst1: list, lst2: list) -> list:
    return list(set(lst1) & set(lst2))

print(intersection([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]


#--------------------------------------------------------------

def fibonacci(n: int) -> list:
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
