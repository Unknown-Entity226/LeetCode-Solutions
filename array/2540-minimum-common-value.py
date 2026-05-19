'''
Problem Description:
Given two integer arrays nums1 and nums2 sorted in non-decreasing order,
return the minimum integer common to both arrays.

If there is no common integer, return -1.

Approach:
- Use two pointers:
    i for nums1
    j for nums2

- Since both arrays are sorted:
    - If nums1[i] == nums2[j]:
          return the value immediately
          (this is the smallest common value)

    - If nums1[i] < nums2[j]:
          move i forward

    - If nums1[i] > nums2[j]:
          move j forward

- If traversal completes without a match,
  return -1.

Time Complexity:
O(n + m)

where:
  n = length of nums1
  m = length of nums2

Space Complexity:
O(1)
'''
class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] > nums2[j]:
                j+=1
            else:
                i+=1
        return -1
