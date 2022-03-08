from collections import deque

"""
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:


Input: root = [3,9,20,null,null,15,7]

Output: 2

Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = deque([root])

        depth = 1

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            depth += 1

        return depth


if __name__ == "__main__":
    lv2l = TreeNode(15)
    lv2r = TreeNode(7)
    lv1l = TreeNode(9)
    lv1r = TreeNode(20, lv2l, lv2r)
    root = TreeNode(3, lv1l, lv1r)
    print("root = [3,9,20,null,null,15,7], output =", Solution().minDepth(root))
