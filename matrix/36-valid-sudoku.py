"""
Problem Description:
Given a partially filled 9 x 9 Sudoku board, determine whether the
filled cells satisfy the Sudoku rules.

Rules:
- Each row can contain digits 1-9 without repetition.
- Each column can contain digits 1-9 without repetition.
- Each 3 x 3 sub-box can contain digits 1-9 without repetition.
- Empty cells are represented by '.' and are ignored.

Approach:
- Maintain three collections to track the digits already seen:
    1. rows[i] stores the digits seen in row i.
    2. cols[j] stores the digits seen in column j.
    3. boxes[b] stores the digits seen in 3 x 3 box b.
- Traverse every cell of the board.
- Ignore empty cells.
- Convert each filled character into an integer.
- Map the digit to index digit - 1 in the corresponding row,
  column, and box.
- If the digit has already been seen in any of the three structures,
  return False.
- Otherwise, mark the digit as present in all three structures.
- If the entire board is processed without finding a duplicate,
  return True.

The 3 x 3 box containing (i, j) is identified using:
    (i // 3) * 3 + (j // 3)

Time Complexity:
O(1)

Reason:
- The board is always fixed at 9 x 9 = 81 cells.
- Therefore, at most 81 cells are examined.

More generally, for an N x N Sudoku board, this would be O(N^2).

Space Complexity:
O(1)

Reason:
- The board size and the number of tracking entries are fixed.
- rows, cols, and boxes each contain 9 lists of size 9.

More generally, for an N x N board, the auxiliary space would be O(N^2).
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        

        rows = {i: [0]*9 for i in range(9)}

        cols ={i: [0]*9 for i in range(9)}

        boxes = {i: [0]*9 for i in range(9)}


        for i in range(9):
            for j in range(9):

                # checker

                if board[i][j] !=".":

                    element = int(board[i][j])
                    if rows[i][element-1] == element or cols[j][element-1] == element or boxes[((i//3)*3+ j //3)][element-1] == element:
                        return False
                    rows[i][element-1] = element
                    cols[j][element-1] = element 
                    boxes[((i//3)*3+ j //3)][element-1] = element

        return True
                

