'''
Problem Description:
A permutation of an array is an arrangement of its elements.
The next permutation is the next lexicographically greater arrangement.

If such a permutation is not possible (i.e., the array is in descending order),
rearrange it to the lowest possible order (ascending).

Approach (As Implemented Below):
- Traverse from right to left to find the first index `i` such that:
      nums[i] < nums[i + 1]
  This identifies the "pivot".

- Once found:
    1. Sort the subarray nums[i+1:] (suffix) in ascending order.
    2. Find the smallest element greater than nums[i] in the suffix.
    3. Swap it with nums[i].

- If no such index exists (array is entirely non-increasing):
    → Reverse the whole array.

Time Complexity:
O(n log n), due to sorting the suffix.

Space Complexity:
O(1), in-place modification (ignoring sort overhead).
'''
class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 2

        while i >= 0:
            if nums[i] < nums[i + 1]:
                nums[i + 1:] = sorted(nums[i + 1:])

                j = len(nums) - 1
                while j > i:
                    if nums[j - 1] <= nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        return
                    j -= 1
            i -= 1

        nums.reverse()
