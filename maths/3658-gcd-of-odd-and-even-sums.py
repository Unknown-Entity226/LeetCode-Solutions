"""
Problem Description:
Given an integer n, compute:
- sumOdd = sum of the first n positive odd numbers.
- sumEven = sum of the first n positive even numbers.
Return the GCD of sumOdd and sumEven.

Approach:
- Use the mathematical formulas:
  - sumOdd = n²
  - sumEven = n(n + 1)
- Compute:
  GCD(n², n(n + 1))
- Factor out n:
  GCD(n², n(n + 1))
  = n × GCD(n, n + 1)
- Since consecutive integers are always coprime,
  GCD(n, n + 1) = 1.
- Therefore, the answer is simply n.

Time Complexity:
O(1)

Reason:
- Only a single return statement is executed.
- No loops or recursion are used.

Space Complexity:
O(1)

Reason:
- Uses only constant extra space.
"""

class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n 
