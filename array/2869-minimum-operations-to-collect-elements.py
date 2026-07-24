"""
Problem Description:
Given an array nums, repeatedly remove the last element
until the collection contains every integer from 1 to k.
Return the minimum number of operations required.

Approach:
- Traverse the array from the end.
- Count each removal as one operation.
- Track which values from 1 to k have been collected.
- Maintain a counter of distinct collected values.
- Stop once all k values have been collected.

Time Complexity:
O(n)

Reason:
- The array is traversed once.
- Each iteration performs only constant-time operations.

Space Complexity:
O(k)

Reason:
- A check array of size k is used to track collected
  numbers.
"""


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        ans = 0

        check = [0]*k

        found = 0
        for i in range(len(nums)-1, -1, -1):

            val = nums[i]
            ans +=1

            if val<=k and check[val-1]== 0:
                check[val-1] = 1
                found +=1
            
            if found == k:
                return ans

        return ans
