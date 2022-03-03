from typing import List


"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j, ans = 0, len(nums) - 1, len(nums)
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                ans = mid
                j = mid - 1
        return ans


if __name__ == "__main__":
    print(Solution().searchInsert(nums=[1, 3, 5, 6], target=5))
    print(Solution().searchInsert(nums=[1, 3, 5, 6], target=2))
    print(Solution().searchInsert(nums=[1, 3, 5, 6], target=7))
