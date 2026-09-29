"""
Problem Description:
Given an integer array, find all unique triplets whose elements sum to zero.
Each triplet must use three different indices, and duplicate triplets must
not appear in the result.

Approach:
- Sort the array.
- Fix one element at a time.
- Use two pointers, left and right, to find two elements whose sum equals
  the negative of the fixed element.
- Skip duplicate values for the fixed element.
- After finding a valid triplet, skip duplicate values from both the left
  and right pointers to prevent duplicate triplets.
- Move both pointers inward and continue searching.

Time Complexity:
O(n^2)

Reason:
- Sorting takes O(n log n).
- For each fixed element, the two-pointer scan takes O(n).
- Therefore the total complexity is O(n^2).

Space Complexity:
O(1) auxiliary space.

Reason:
- Apart from the returned result, only a constant number of variables
  are used.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()

        ans = []

        for x in range(len(nums)):
            print(x)
            if  x>0 and  nums[x] == nums[x-1]:
                continue
            left = x+1
            right = len(nums)-1
            target = 0-nums[x]
            while left<right:
                if nums[left]+ nums[right] == target:
                    ans.append([nums[x], nums[left], nums[right]])

                    while left<right and nums[left]== nums[left+1]:
                        left+=1

                    while left<right and nums[right] == nums[right-1]:
                        right-=1
                        
                    left+=1
                    right-=1
                
                elif nums[left]+nums[right]>target:
                    right-=1
                else:
                    left+=1
                
        return ans
