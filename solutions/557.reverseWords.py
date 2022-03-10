"""
557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

Input: s = "God Ding"
Output: "doG gniD"

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        words = s.split(" ")
        for word in words:
            chars = list(word)
            chars.reverse()
            ans.append("".join(chars))
        return " ".join(ans)

if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print("Input: s=", s)
    print("Output:", Solution().reverseWords(s))
    s = "God Ding"
    print("Input: s=", s)
    print("Output:", Solution().reverseWords(s))