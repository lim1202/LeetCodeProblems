"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        n = len(s)
        ans, cur = 0, -1
        for i in range(n):
            if i != 0:
                chars.remove(s[i - 1])
            while cur + 1 < n and s[cur + 1] not in chars:
                chars.add(s[cur + 1])
                cur += 1
            ans = max(ans, cur - i + 1)
        return ans


if __name__ == "__main__":
    s = Solution()
    print('Input: s = "abcabcbb"')
    print("Output:", s.lengthOfLongestSubstring("abcabcbb"))
    print('Input: s = "bbbbb"')
    print("Output:", s.lengthOfLongestSubstring("bbbbb"))
    print('Input: s = "pwwkew"')
    print("Output:", s.lengthOfLongestSubstring("pwwkew"))
