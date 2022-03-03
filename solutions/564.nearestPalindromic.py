"""
564. Find the Closest Palindrome

Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.

Constraints:

1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 10^18 - 1].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-closest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        if m == 1:
            return str(int(n) - 1)

        candidates = [10 ** (m - 1) - 1]
        selfPrefix = int(n[: (m + 1) // 2])

        for x in range(selfPrefix - 1, selfPrefix + 2):
            y = x if m % 2 == 0 else x // 10
            y = str(y)[::-1] if y > 9 else y
            candidates.append(int(str(x) + str(y)))

        ans = 10**m + 1
        selfNumber = int(n)
        for candidate in candidates:
            if candidate != selfNumber:
                if (
                    abs(candidate - selfNumber) < abs(ans - selfNumber)
                    or abs(candidate - selfNumber) == abs(ans - selfNumber)
                    and candidate < ans
                ):
                    ans = candidate
        return str(ans)


if __name__ == "__main__":
    print(Solution().nearestPalindromic("1"))
    print(Solution().nearestPalindromic("2"))
    print(Solution().nearestPalindromic("10"))
    print(Solution().nearestPalindromic("123"))
    print(Solution().nearestPalindromic("1213"))
