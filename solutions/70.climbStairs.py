"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        i, j, k = 0, 0, 1

        for _ in range(n):
            i = j
            j = k
            k = i + j

        return k


if __name__ == "__main__":
    print("Input: n = 2")
    print("Output:", Solution().climbStairs(2))
    print("Input: n = 3")
    print(Solution().climbStairs(3))
