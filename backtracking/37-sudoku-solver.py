"""
Problem Description:
Solve a 9 x 9 Sudoku puzzle by filling empty cells such that
every row, column, and 3 x 3 sub-box contains digits 1 through 9
exactly once.

Approach:
- Maintain sets for the digits already present in each row,
  column, and 3 x 3 box.
- Store the coordinates of all empty cells.
- Use backtracking to fill the empty cells one by one.
- Try digits from 1 to 9 that do not violate any Sudoku constraint.
- If a choice leads to a dead end, undo the placement and try
  the next digit.
- Stop when every empty cell has been filled successfully.

Time Complexity:
O(9^E), where E is the number of empty cells.

Reason:
- Each empty cell can have at most 9 candidate digits.
- In the worst case, backtracking explores up to 9 choices per
  empty cell, giving O(9^E).
- Checking row, column, and box membership takes O(1) on average
  because the sets contain at most 9 elements.

Space Complexity:
O(E)

Reason:
- The empty_cells list stores E coordinates.
- The recursion depth can reach E.
- The row, column, and box sets have fixed sizes for a 9 x 9 board,
  so their space usage is O(1) with respect to E.
"""
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    b = 3 * (r // 3) + (c // 3)
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[b].add(val)
                else:
                    empty_cells.append((r, c))
        def backtrack(k: int) -> bool:
            if k == len(empty_cells):
                return True

            r, c = empty_cells[k]
            b = 3 * (r // 3) + (c // 3)

            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

                    if backtrack(k + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[b].remove(num)

            return False

        backtrack(0)
