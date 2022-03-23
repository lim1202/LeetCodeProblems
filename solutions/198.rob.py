"""
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums is None:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            first, second = second, max(first + nums[i], second)

        return second


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 1]
    print("Input: nums =", nums)
    print("Output:", s.rob(nums))
    nums = [2, 7, 9, 3, 1]
    print("Input: nums =", nums)
    print("Output:", s.rob(nums))
