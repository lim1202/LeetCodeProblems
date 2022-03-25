"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 1]
    print("Input: nums =", nums)
    print("Output:", sol.singleNumber(nums))
    nums = [4, 1, 2, 1, 2]
    print("Input: nums =", nums)
    print("Output:", sol.singleNumber(nums))
    nums = [1]
    print("Input: nums =", nums)
    print("Output:", sol.singleNumber(nums))