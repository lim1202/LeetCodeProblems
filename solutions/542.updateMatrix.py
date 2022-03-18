"""
542. 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/01-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        # 初始化结果矩阵
        dist = [[10**9] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0

        # 只有 水平向左移动 和 竖直向上移动
        for i in range(m):
            for j in range(n):
                for x, y in [(i - 1, j), (i, j - 1)]:
                    if x >= 0 and y >= 0:
                        dist[i][j] = min(dist[i][j], dist[x][y] + 1)

        # 只有 水平向右移动 和 竖直向下移动
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                for x, y in [(i + 1, j), (i, j + 1)]:
                    if x < m and y < n:
                        dist[i][j] = min(dist[i][j], dist[x][y] + 1)

        return dist


if __name__ == "__main__":
    s = Solution()
    print("Input: mat = [[0,0,0],[0,1,0],[0,0,0]]")
    print("Output:", s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print("Input: mat = [[0,0,0],[0,1,0],[1,1,1]]")
    print("Output:", s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
