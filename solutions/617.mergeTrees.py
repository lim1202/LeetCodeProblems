"""
617. Merge Two Binary Trees

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Example 1:

Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]

Constraints:

The number of nodes in both trees is in the range [0, 2000].
-104 <= Node.val <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-binary-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self, depth=0) -> str:
        ret = []
        q = deque([self])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if not node:
                    ret.append(node)
                    continue
                ret.append(node.val)
                if node.left or node.right:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return str(ret)


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged

if __name__ == "__main__":
    root1 = TreeNode(1, TreeNode(3, TreeNode(2), TreeNode(5)))
    root2 = TreeNode(2, TreeNode(1, TreeNode(3), None), TreeNode(4, None, TreeNode(7)))
    print("Input: root1 =", root1, ", root2 =", root2)
    print("Output:", Solution().mergeTrees(root1, root2))
