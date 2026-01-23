'''
LeetCode 6: Zigzag Conversion
Topics: String, Simulation

Problem Description:
Given a string s and an integer numRows, write the string in a zigzag
pattern across numRows rows and then read the pattern row by row.

The zigzag pattern moves:
- Vertically down the rows
- Then diagonally up until the top row
- Repeats this pattern until all characters are placed

Approach:
- Handle the edge case where numRows is 1 or numRows is greater than or
  equal to the length of the string (no zigzag needed).
- Create a list of lists (matrix) where each inner list represents a row.
- Use a flag to track direction:
  - flag = True  → moving downwards
  - flag = False → moving upwards diagonally
- Traverse the string using an index:
  - Append each character to the current row.
  - Move the row pointer up or down based on the direction.
  - Change direction when the top or bottom row is reached.
- Finally, concatenate all rows to form the result string.

Time Complexity:
O(n), where n is the length of the string.'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s 
        matrix = [[] for _ in range(numRows)]
        matrix[0].append(s[0])
        flag = True
        result = ""
        row = 1
        index = 1

        while index < len(s):
            if flag:
                matrix[row].append(s[index])
                row += 1
                index += 1
                if row == numRows:
                    flag = False
                    row -= 2
            else:
                matrix[row].append(s[index])
                row -= 1
                index += 1
                if row == -1:
                    flag = True
                    row += 2
            
        for r in matrix:
            result += "".join(r)

        return result
