from collections import deque
from typing import List

"""
752. Open the Lock

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,

because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".

Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.

Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/open-the-lock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        dead = set(deadends)
        if "0000" in dead:
            return -1

        q = deque([("0000", 0)])

        visited = set(deadends)
        visited.add("0000")

        while q:
            code, step = q.popleft()
            if code in deadends:
                continue
            if code == target:
                return step
            for next_code in self.getNext(code):
                if next_code not in visited:
                    q.append((next_code, step + 1))
                    visited.add(next_code)
        return -1

    def getNext(self, code: str) -> List[str]:
        res = []
        for i in range(4):
            up = self.plusOne(code, i)
            down = self.minusOne(code, i)
            res.append(up)
            res.append(down)
        return res

    def plusOne(self, code: str, i: int) -> str:
        nums = list(code)
        nums[i] = str(int(nums[i]) + 1) if int(nums[i]) < 9 else "0"
        return "".join(nums)

    def minusOne(self, code: str, i: int) -> str:
        nums = list(code)
        nums[i] = str(int(nums[i]) - 1) if int(nums[i]) > 0 else "9"
        return "".join(nums)


if __name__ == "__main__":
    print(
        'deadends=["0201", "0101", "0102", "1212", "2002"], target="0202", output=',
        Solution().openLock(
            deadends=["0201", "0101", "0102", "1212", "2002"], target="0202"
        ),
    )
    print(
        'deadends=["8888"], target="0009", output=',
        Solution().openLock(deadends=["8888"], target="0009"),
    )
    print(
        'deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], target="8888", output=',
        Solution().openLock(
            deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"],
            target="8888",
        ),
    )
