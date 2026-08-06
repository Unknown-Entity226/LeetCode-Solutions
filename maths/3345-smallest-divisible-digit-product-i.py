"""
Problem Description:
Given two integers n and t, find the smallest integer
greater than or equal to n such that the product of its
digits is divisible by t.

Approach:
- Starting from n, compute the product of its digits.
- If the product is divisible by t, return the number.
- Otherwise, increment the number and repeat.

Time Complexity:
O(k × d)

Reason:
- Let k be the number of integers checked until the
  answer is found.
- Let d be the number of digits in each number.
- Computing the digit product takes O(d) for each
  candidate.

Space Complexity:
O(1)

Reason:
- Only a constant number of variables are used.
"""
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def check(num):
            product = 1
            while num:
                product*=num%10
                num//=10
            return product

        while True:
            if check(n)%t == 0:
                return n
            else:
                n+=1
