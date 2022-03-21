"""
784. Letter Case Permutation

Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]

Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-case-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.res = []
        chars = list(s)
        self.backtrack(chars, [])
        return self.res

    def backtrack(self, chars: List[str], track: List[str]):
        if not chars or len(chars) == 0:
            self.res.append("".join(track))
            return

        char = chars[0]
        remains = chars[1:]
        if char.isdigit():
            track.append(char)
            self.backtrack(remains, track)
            track.pop()
        else:
            track.append(char.lower())
            self.backtrack(remains, track)
            track.pop()
            track.append(char.upper())
            self.backtrack(remains, track)
            track.pop()


if __name__ == "__main__":
    print('Input: s = "a1b2"')
    print(Solution().letterCasePermutation("a1b2"))
    print('Input: s = "3z4"')
    print(Solution().letterCasePermutation("3z4"))
