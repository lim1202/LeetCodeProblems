"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:

Input: n = 1, k = 1
Output: [[1]]

Constraints:

1 <= n <= 20
1 <= k <= n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        if k <= 0 or n < k:
            return ans
        path = []
        self.dfs(1, n, k, path, ans)
        return ans

    def dfs(self, start: int, n: int, k: int, path: List[int], ans: List[List[int]]):
        if k == 0:
            ans.append(path[:])
            return

        if start > n - k + 1:
            return

        self.dfs(start + 1, n, k, path, ans)
        path.append(start)
        self.dfs(start + 1, n, k - 1, path, ans)
        path.pop()


if __name__ == "__main__":
    print("Input: n = 4, k = 2")
    print("Output:", Solution().combine(4, 2))
    print("Input: n = 1, k = 1")
    print("Output:", Solution().combine(1, 1))
