"""
Problem Description:
Given an integer array nums, return the kth largest element
in the array without sorting.

Approach:
- Convert nums into a max heap using bottom-up heap construction.
- Repeatedly remove the maximum element from the heap.
- After k removals, the last removed element is the kth
  largest element.
- Use heapify to restore the max-heap property after each
  removal.

Time Complexity:
O(n + k log n)

Reason:
- Bottom-up heap construction takes O(n).
- Each heapPop takes O(log n) in the worst case.
- Performing k removals takes O(k log n).
- Therefore, total complexity is O(n + k log n).

Space Complexity:
O(1)

Reason:
- The heap is constructed directly inside nums.
- No additional array or data structure proportional to n
  is created.
"""
class Solution:

    def heapify(self, arr, size, index):

        while index < size:

            left = 2 * index + 1
            right = 2 * index + 2

            largest = index

            if left < size and arr[left] > arr[largest]:
                largest = left
            if right < size and arr[right] > arr[largest]:
                largest = right
            if largest == index:
                break

            arr[index], arr[largest] = (
                arr[largest],
                arr[index],
            )
            index = largest

    def buildHeapFromArray(self, arr):

        index = len(arr)// 2 - 1
        while index>=0:
            self.heapify(arr, len(arr), index)
            index-=1
    def heapPop(self, arr):

        if not arr:
            return -1
        if len(arr)==1:
            return arr.pop()
        root = arr[0]

        arr[0] = arr.pop()
        index = 0

        self.heapify(arr, len(arr), index)
        return root

    def findKthLargest(self, nums: List[int], k: int) -> int:        
        
        self.buildHeapFromArray(nums)

        for _ in range(k):
            result = self.heapPop(nums)
        return result
