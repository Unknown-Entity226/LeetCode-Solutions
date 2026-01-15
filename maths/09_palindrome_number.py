'''
Problem Description:
Given an integer x, return true if x is a , and false otherwise.

Approach:
->Negative numbers cannot be palindromes.
->Any number ending in 0 (except 0 itself) cannot be a palindrome.
->Reverse only half of the number instead of the entire number.
->Stop reversing when the reversed half becomes greater than or equal to the remaining half.
->For numbers with:
->Even digits: both halves should be equal.
->Odd digits: ignore the middle digit before comparison.
Time Complexity: O(d), where d is the number of digits in x
'''
#Python Implementation
class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x>rev:
            rev = rev*10+x%10
            x//=10
        return x== rev or x == rev//10
