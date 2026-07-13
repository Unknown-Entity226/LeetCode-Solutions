"""
Problem Description:
Given two sorted 2D arrays containing [id, value] pairs,
merge them into a single sorted array. If an id appears
in both arrays, sum their values.

Approach:
- Use two pointers to traverse both arrays.
- Compare the current ids:
  - Smaller id → add it to the answer.
  - Equal ids → add the id with the summed value.
- Move the corresponding pointer(s).
- Append any remaining elements after one array is exhausted.

Time Complexity:
O(n + m)

Reason:
- n = length of nums1.
- m = length of nums2.
- Each element from both arrays is processed exactly once.

Space Complexity:
O(n + m)

Reason:
- The answer array stores all unique ids.
- Excluding the returned output, the algorithm uses O(1)
  auxiliary space.
"""
class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
         
        i= 0
        j = 0

        while i<len(nums1) and j<len(nums2):
            if nums1[i][0]<nums2[j][0]:
                ans.append(nums1[i])
                i+=1
            elif  nums1[i][0]>nums2[j][0]:
                ans.append(nums2[j])
                j+=1
            else:
                ans.append([nums1[i][0], nums1[i][1]+nums2[j][1]])
                i+=1
                j+=1
        while i<len(nums1):
            ans.append(nums1[i])
            i+=1
        while j<len(nums2):
            ans.append(nums2[j])
            j+=1
        return ans
