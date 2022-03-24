"""
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:

Input: n = 3
Output: false

Constraints:

-231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n - 1) == 0


if __name__ == "__main__":
    solu = Solution()
    print("Input: n = 1")
    print(solu.isPowerOfTwo(1))
    print("Input: n = 16")
    print(solu.isPowerOfTwo(16))
    print("Input: n = 3")
    print(solu.isPowerOfTwo(3))
