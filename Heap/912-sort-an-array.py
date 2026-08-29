"""
Problem Description:
Given an integer array nums, sort the array in ascending
order without using the built-in sorting function.

Approach:
- Build a max heap from the input array using bottom-up
  heap construction.
- Repeatedly swap the maximum element at the root with the
  last element in the unsorted portion of the array.
- Reduce the heap size and restore the max-heap property
  using heapify.
- Since the maximum elements are placed at the end one by
  one, the final array is sorted in ascending order.

Time Complexity:
O(n log n)

Reason:
- Building the max heap takes O(n).
- Heap sort performs n-1 extractions.
- Each extraction requires O(log n) heapify.
- Therefore, total complexity is O(n + n log n)
  = O(n log n).

Space Complexity:
O(1)

Reason:
- The heap is built directly inside nums.
- Heapify is iterative, so there is no recursion stack.
- No additional array proportional to n is used.
"""
class Solution:

    def buildHeap(self, arr):

        index = len(arr)//2-1

        while index>=0:
            self.heapify(arr, len(arr), index)
            index-=1

    def heapify(self, arr, size, index):
        while index<size:

            left = 2*index+1
            right = 2*index +2

            largest = index

            if left<size and arr[left]>arr[largest]:
                largest = left
            if right <size and arr[right]>arr[largest]:
                largest = right
            if largest == index:
                break
            
            arr[index], arr[largest] = arr[largest], arr[index]
            index = largest
    
    def heapSort(self, arr):
        size = len(arr)

        while size>1:
            arr[0], arr[size-1] = arr[size-1], arr[0]
            size-=1
            self.heapify(arr, size, 0)
            

    def sortArray(self, nums: List[int]) -> List[int]:
        
        self.buildHeap(nums)
        self.heapSort(nums)
        return nums
