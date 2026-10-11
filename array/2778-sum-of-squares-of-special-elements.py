
"""
Problem Description:
Given a 1-indexed integer array nums of length n, an element nums[i]
is special if n is divisible by its 1-based index i.
Return the sum of squares of all special elements.

Approach:
- Let n be the length of nums.
- Iterate through the array using 0-based indices.
- Convert each index i to its corresponding 1-based index i + 1.
- If n % (i + 1) == 0, the element is special.
- Add nums[i] * nums[i] to the answer.
- Return the accumulated sum.

Time Complexity:
O(n)

Reason:
- Every element is visited exactly once.

Space Complexity:
O(1)

Reason:
- Only a constant number of extra variables are used.
"""

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        
        n = len(nums)

        ans = 0

        for i in range(n):
            if n%(i+1) == 0:
                ans+= nums[i]*nums[i]

        return ans
