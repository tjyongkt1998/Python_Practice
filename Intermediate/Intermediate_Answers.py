#------------------------------------------------------------
def binary_search(lst: list, target: int) -> int:
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 2, 3, 4, 5], 3))  # Output: 2


#------------------------------------------------------------
def rotate_matrix(matrix: list) -> list:
    return [list(reversed(col)) for col in zip(*matrix)]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(rotate_matrix(matrix))
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


#------------------------------------------------------------
def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

print(is_valid_parentheses("()[]{}"))  # Output: True
print(is_valid_parentheses("(]"))      # Output: False


#------------------------------------------------------------
from collections import defaultdict

def group_anagrams(strs: list) -> list:
    anagrams = defaultdict(list)
    for s in strs:
        sorted_s = "".join(sorted(s))
        anagrams[sorted_s].append(s)
    return list(anagrams.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


#------------------------------------------------------------
def length_of_longest_substring(s: str) -> int:
    char_index = {}
    max_length = start = 0
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_length = max(max_length, i - start + 1)
    return max_length

print(length_of_longest_substring("abcabcbb"))  # Output: 3


#------------------------------------------------------------
def find_duplicates(nums: list) -> list:
    duplicates = []
    for num in nums:
        if nums[abs(num) - 1] < 0:
            duplicates.append(abs(num))
        else:
            nums[abs(num) - 1] *= -1
    return duplicates

print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # Output: [2, 3]


#------------------------------------------------------------
def product_except_self(nums: list) -> list:
    length = len(nums)
    left, right, output = [1]*length, [1]*length, [1]*length
    for i in range(1, length):
        left[i] = left[i-1] * nums[i-1]
    for i in range(length-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]
    for i in range(length):
        output[i] = left[i] * right[i]
    return output

print(product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]


#------------------------------------------------------------
import json

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: TreeNode) -> str:
    def helper(node):
        if node is None:
            return None
        return [node.val, helper(node.left), helper(node.right)]
    return json.dumps(helper(root))

def deserialize(data: str) -> TreeNode:
    def helper(lst):
        if lst is None:
            return None
        node = TreeNode(lst[0])
        node.left = helper(lst[1])
        node.right = helper(lst[2])
        return node
    return helper(json.loads(data))

# Example usage:
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
serialized = serialize(root)
print(serialized)  # Output: JSON representation
deserialized = deserialize(serialized)


#------------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example usage:
node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node2.next = node1  # Creates a cycle
print(has_cycle(node1))  # Output: True


#------------------------------------------------------------
def permute(s: str) -> list:
    if len(s) == 1:
        return [s]
    permutations = []
    for i, char in enumerate(s):
        for perm in permute(s[:i] + s[i+1:]):
            permutations.append(char + perm)
    return permutations

print(permute("abc"))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

#------------------------------------------------------------

