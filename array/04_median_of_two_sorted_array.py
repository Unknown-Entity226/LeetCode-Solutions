'''
Description:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Approach:
Combine both input arrays into a single list.
Sort the merged list.
If the total number of elements is:
Even: return the average of the two middle elements.
Odd: return the middle element directly.
Time Complexity: O((m + n) log(m + n))
Space Complexity: O(m + n)'''

#Python Implementation
code
