'''Problem Description:
Given a sorted integer array nums (non-decreasing order),
remove the duplicates in-place such that each unique element
appears only once.

The relative order of elements must be maintained.
Return the number of unique elements k.

After the operation:
- The first k elements of nums should contain the unique elements
  in sorted order.
- Elements beyond index k-1 can be ignored.

Approach:
- Since the array is already sorted, all duplicates appear consecutively.
- Use a write pointer to track the position where the next unique element
  should be placed.
- Traverse the array:
  - If the current element is different from the previous element,
    write it at the write pointer index and increment the pointer.
- The write pointer value at the end represents the count of unique elements.

Time Complexity:
O(n), where n is the length of nums (single pass).

Space Complexity:
O(1), since the operation is done in-place.'''

class Solution(object):
    def removeDuplicates(self, nums):
        prev = None
        write = 0
        for num in nums:
            if prev is None or num != prev:
                nums[write] = num
                write += 1
            prev = num
        return write
