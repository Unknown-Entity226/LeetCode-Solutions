"""
Problem Description:
Given the heights of bars in a histogram, find the area
of the largest rectangle that can be formed.

Approach:
- Compute the Previous Smaller Element (PSE) index for
  every bar.
- Compute the Next Smaller Element (NSE) index for every
  bar.
- For each bar:
  - Treat it as the smallest bar in the rectangle.
  - Width = NSE - PSE - 1.
  - Area = height × width.
- Return the maximum area obtained.

Time Complexity:
O(n)

Reason:
- Computing PSE takes O(n).
- Computing NSE takes O(n).
- Final traversal takes O(n).
- Each index is pushed and popped at most once.

Space Complexity:
O(n)

Reason:
- Previous and Next arrays each store n indices.
- Stack stores at most n indices.
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        def nextSmaller(arr):
            stack = [-1]
            ans = [0]*len(arr)

            for i in range(len(arr)-1, -1, -1):
                while stack[-1]!=-1 and arr[stack[-1]]>=arr[i]:
                    stack.pop()
                
                ans[i] = stack[-1]

                stack.append(i)

            return ans
        def prevSmaller(arr):
            stack = [-1]
            ans = []

            for i in range(len(arr)):
                while stack[-1]!=-1 and arr[stack[-1]]>=arr[i]:
                    stack.pop()
                
                ans.append(stack[-1])

                stack.append(i)
                
            return ans


        n =len(heights)

        next = nextSmaller(heights)
        prev = prevSmaller(heights)

        area = float("-inf")

        for i in range(n):
            length = heights[i]

            if next[i] == -1:
                next[i] = n
            
            width = next[i]-prev[i]-1

            area = max(area, length*width)
        return area
