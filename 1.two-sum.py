#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i, j];

    def twoSum(self, nums, target):
        D = {}
        for i in range(len(nums)):
            if target - nums[i] in D:
                return [D[target - nums[i]], i]
            
            D[nums[i]] = i
# @lc code=end