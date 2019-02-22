''''
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
palindroms = []
def is_palindrom(num):
    return str(num) == str(num)[::-1]

nums1 = list(x for x in range(999,0,-1))
nums2 = list(y for y in range(999,0,-1))

for x in nums1:
    for y in nums2:
        result = x*y
        if is_palindrom(result):
            palindroms.append(result)

print(max(palindroms))
