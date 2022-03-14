"""
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m > n:
            return False

        cnt1 = dict()
        cnt2 = dict()

        for i in range(m):
            cnt1[s1[i]] = 1 if cnt1.get(s1[i]) is None else cnt1[s1[i]] + 1
            cnt2[s2[i]] = 1 if cnt2.get(s2[i]) is None else cnt2[s2[i]] + 1

        if cnt1 == cnt2:
            return True

        for j in range(m, n):
            cnt2[s2[j]] = 1 if cnt2.get(s2[j]) is None else cnt2[s2[j]] + 1
            if cnt2[s2[j - m]] == 1:
                del cnt2[s2[j - m]]
            else:
                cnt2[s2[j - m]] = cnt2[s2[j - m]] - 1

            if cnt1 == cnt2:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print('Input: s1 = "ab", s2 = "eidbaooo"')
    print("Output:", s.checkInclusion("ab", "eidbaooo"))
    print('Input: s1 = "ab", s2 = "eidboaoo"')
    print("Output:", s.checkInclusion("ab", "eidboaoo"))
