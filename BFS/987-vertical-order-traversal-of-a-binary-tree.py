"""
Problem Description:
Given the root of a binary tree, return its vertical
order traversal.

Each node has a position (row, col):
- Left child  -> (row + 1, col - 1)
- Right child -> (row + 1, col + 1)

Nodes must be returned:
- From the leftmost column to the rightmost column.
- Within each column, from top to bottom.
- If multiple nodes have the same row and column, sort
  them by their values.

Approach:
- Use BFS to traverse the tree while storing each node's
  row and column.
- Store node values using:
    column -> row -> values
- After traversal:
  - Process columns from left to right.
  - Process rows from top to bottom.
  - Sort values when multiple nodes share the same
    row and column.
- Flatten the values of each column into the result.

Time Complexity:
O(n log n)

Reason:
- BFS visits every node in O(n).
- Column keys and row keys are sorted.
- Values sharing the same position are sorted.
- Overall sorting contributes O(n log n) in the worst case.

Space Complexity:
O(n)

Reason:
- The hash map stores every node's value and coordinates.
- The BFS queue can also contain O(n) nodes.
"""


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque, defaultdict
        colDict = defaultdict(lambda: defaultdict(list))

        ans = []
        if not root:
            return ans

        q = deque()
        q.append([root, (0, 0)])

        while q:
            v = q.popleft()
            node, row, col = v[0], v[1][0], v[1][1]
            
        
            colDict[col][row].append(node.val)

            if node.left:
                q.append([node.left,(row+1, col-1)])
            if node.right:
                q.append([node.right,(row+1, col+1)])

        for c in sorted(colDict.keys()):
            col_vals = []
            for r in sorted(colDict[c].keys()):
                col_vals.extend(sorted(colDict[c][r]))
            ans.append(col_vals)        

        return ans

