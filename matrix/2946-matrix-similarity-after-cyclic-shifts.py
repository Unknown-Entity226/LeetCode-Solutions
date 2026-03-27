'''
Problem Description:
You are given an m x n matrix `mat` and an integer k.

The following process is applied k times:
- Even-indexed rows (0, 2, 4, ...) are cyclically shifted LEFT.
- Odd-indexed rows (1, 3, 5, ...) are cyclically shifted RIGHT.

After k operations, determine if the matrix becomes identical
to the original matrix.

Approach:
- A cyclic shift by k steps can be simulated using modulo arithmetic.
- For each row:
    - Even row → left shift → index becomes (j + k) % n
    - Odd row  → right shift → index becomes (j - k) % n

- Instead of modifying the matrix k times,
  directly check whether each element maps back to its original position.

- If any mismatch is found → return False.
- If all elements match → return True.

Time Complexity:
O(m * n), where m = number of rows, n = number of columns.

Space Complexity:
O(1), no extra space used.
'''
class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        n = len(mat[0])

        for i in range(len(mat)):
            for j in range(n):
                if i % 2 == 0:
                    # Even row → left shift
                    if mat[i][(j + k) % n] != mat[i][j]:
                        return False
                else:
                    # Odd row → right shift
                    if mat[i][(j - k) % n] != mat[i][j]:
                        return False

        return True
