"""
Problem Description:
Construct an array prefixGcd where:
- prefixGcd[i] = gcd(nums[i], maximum element seen up to index i).
Sort the array and repeatedly pair the smallest and
largest remaining elements. Return the sum of the GCD
of every formed pair.

Approach:
- Traverse the array while maintaining the prefix maximum.
- Compute gcd(current element, current prefix maximum)
  for each index and store it.
- Sort the prefixGcd array.
- Use two pointers:
  - Left points to the smallest element.
  - Right points to the largest element.
- Add the GCD of each pair to the answer.
- If the array length is odd, the middle element is
  automatically ignored.

Time Complexity:
O(n log n)

Reason:
- Constructing prefixGcd takes O(n).
- Each GCD computation takes O(log M), where M is the
  maximum value in nums.
- Sorting dominates with O(n log n).
- Pairing using two pointers takes O(n).

Space Complexity:
O(n)

Reason:
- prefixGcd stores n elements.
- Excluding the recursion stack (none) and the output.
"""

class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(n, m):
            while m:
                n, m = m, n%m
            return n
        prefixGcd = []

        m = nums[0]

        for i in nums:
            m = max(i, m)
            prefixGcd.append(gcd(i,m ))
        prefixGcd.sort()

        start = 0
        end = len(prefixGcd)-1
        total = 0
        while start<end:

            total+= gcd(prefixGcd[start], prefixGcd[end])
            start+=1
            end-=1
        return total

