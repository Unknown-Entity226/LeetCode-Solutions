'''
Problem Description:
Given the root of a binary tree,
return the preorder traversal of its nodes' values.

Preorder traversal follows:
    Root → Left → Right

Approach:
- Use recursive DFS traversal.
- For each node:
    1. Visit the current node and add its value.
    2. Traverse the left subtree.
    3. Traverse the right subtree.

- Store traversal values in a result list.

Time Complexity:
O(n), where n is the number of nodes.

Space Complexity:
O(h), where h is the height of the tree
due to recursion stack.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def preOrder(root):
            if root:
                result.append(root.val)
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return result
