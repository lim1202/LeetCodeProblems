"""
509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:

0 <= n <= 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fibonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        dp_i_1 = 1
        dp_i_2 = 0
        dp_i = 1
        for i in range(2, n):
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
            dp_i = dp_i_1 + dp_i_2

        return dp_i

if __name__ == "__main__":
    print(Solution().fib(2))
    print(Solution().fib(3))
    print(Solution().fib(4))
