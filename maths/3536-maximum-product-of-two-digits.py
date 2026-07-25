"""
Problem Description:
You are given a positive integer n.
Return the maximum product of any two digits in n.
Note: You may use the same digit twice if it appears more than once in n.

Approach Used:
-Take 2 variables -> l and s
-Iterate through all the digits in the number
-compare digit with l and s
-store largest digit in l and second largest in s

Time Complexity:
O(d)
- where d is the no of digits in the number

Space Complexity:
O(1)

- No extra space is being used.
"""

class Solution:
    def maxProduct(self, n: int) -> int:
        
        l = 0
        s = 0

        while n:

            digit = n%10
            if digit>=l:
                s = l
                l = digit


            elif digit>s:
                s = digit
            n//=10

        return l*s
