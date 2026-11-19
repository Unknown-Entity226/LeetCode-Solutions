"""
Problem Description:
Given the root of a binary tree, return all paths from the root node
to every leaf node.

A leaf node is a node that has no left or right child.

Approach:
Use Depth-First Search (DFS) with backtracking.

1. Maintain a path list to store the values of the current root-to-node path.
2. Append the current node's value to the path.
3. If the current node is a leaf:
   - Join the path elements using "->".
   - Append the resulting string to the output list.
   - Return.
4. If the current node has a left child, recursively explore it.
5. Backtrack by removing the current node's value from the path.
6. If the current node has a right child, recursively explore it.
7. Backtrack again after exploring the right subtree.

Time Complexity: O(n * h)
Reason: Every node is visited once. Constructing a path string at each
leaf requires time proportional to the path length, which is at most h.
For a binary tree, this is O(n * h) in the worst case.

Space Complexity: O(h) auxiliary space, excluding output.
Reason: The recursion stack and current path can each contain at most h
nodes, where h is the height of the tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        
        output = []

        def backtrack(node, path):

            path.append(str(node.val))

            if not node.left and not node.right:
                
                output.append("->".join(path))
                return 


            if node.left:
                backtrack(node.left, path)
                path.pop()
        
            if node.right: 
                backtrack(node.right, path)
                path.pop()


        backtrack(root, [])

        return output
