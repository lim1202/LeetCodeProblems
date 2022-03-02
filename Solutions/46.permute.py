from typing import List

"""
46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, [])
        return self.res

    def backtrack(self, nums: List[int], track: List[int]):
        if not nums or len(nums) == 0:
            self.res.append(track[:])
            return

        for num in nums:
            track.append(num)
            remains = nums[:]
            remains.remove(num)
            self.backtrack(remains, track)
            track.pop()

if __name__ == "__main__":
    print(Solution().permute([1,2,3]))