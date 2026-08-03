"""
Problem Description:
Given an integer n, return the difference between the
product of its digits and the sum of its digits.

Approach:
- Extract each digit using modulo and integer division.
- Maintain:
  - The sum of all digits.
  - The product of all digits.
- Return (product - sum).

Time Complexity:
O(d)

Reason:
- d = number of digits in n.
- Each digit is processed exactly once.

Space Complexity:
O(1)

Reason:
- Only a constant number of variables are used.
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        s = 0
        m = 1

        while n:
            digit = n%10
            s+=digit
            m*=digit
            n//=10
        return m-s
