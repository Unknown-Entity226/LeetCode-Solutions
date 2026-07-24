"""
Problem Description:
Given a binary matrix, find the area of the largest
rectangle containing only 1's.

Approach:
- Treat each row as the base of a histogram.
- Convert the matrix into histogram heights by
  accumulating consecutive 1's column-wise.
- For every row:
  - Compute the largest rectangle in its histogram using
    the monotonic stack approach.
- Return the maximum area among all rows.

Time Complexity:
O(rows × cols)

Reason:
- Updating histogram heights for each row takes O(cols).
- Largest Rectangle in Histogram for each row takes O(cols).
- Repeated for all rows.

Space Complexity:
O(cols)

Reason:
- The histogram algorithm uses Previous Smaller,
  Next Smaller, and a stack, each of size at most cols.
- The input matrix is modified in-place, so no additional
  O(rows × cols) space is used.
"""

class Solution:

    def largestRectangleArea(self, arr:list[int])->int:

        def nextSmaller(arr: list[int])->list[int]:
            stack = [-1]
            ans = [0]*len(arr)

            for i in range(len(arr)-1, -1, -1):
                while stack[-1]!=-1 and arr[stack[-1]]>=arr[i]:
                    stack.pop()
                
                ans[i] = stack[-1]

                stack.append(i)

            return ans
        def prevSmaller(arr:list[int])->list[int]:
            stack = [-1]
            ans = []

            for i in range(len(arr)):
                while stack[-1]!=-1 and arr[stack[-1]]>=arr[i]:
                    stack.pop()
                
                ans.append(stack[-1])

                stack.append(i)
                
            return ans


        n =len(arr)

        next = nextSmaller(arr)
        prev = prevSmaller(arr)

        area = float("-inf")

        for i in range(n):
            length = arr[i]

            if next[i] == -1:
                next[i] = n
            
            width = next[i]-prev[i]-1

            area = max(area, length*width)
        return area

    def maximalRectangle(self, matrix: list[list[str]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        matrix = [list(map(int, i)) for i in matrix]

        area = self.largestRectangleArea(matrix[0])

        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(1,rows):
            for j in range(cols):

                if matrix[i][j] !=0:
                    matrix[i][j]+= matrix[i-1][j]


            area = max(area, self.largestRectangleArea(matrix[i]))

        return area
