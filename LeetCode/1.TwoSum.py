"""
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


def myanswer(nums, target):
    for i, v1 in enumerate(nums):
        for j, v2 in enumerate(nums[i + 1:]):
            if v1 + v2 == target:
                return [i, j + i + 1]


'''
建立字典 lookup 存放第一个数字，并存放该数字的 index
判断 lookup 种是否存在： target - 当前数字， 则表面 当前值和 lookup中的值加和为 target.
如果存在，则返回： target - 当前数字 的 index 和 当前值的 index
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(myanswer(nums, target))
    # solution = Solution()
    print(Solution().twoSum(nums=nums, target=target))
