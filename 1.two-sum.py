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
        D = {}
        for i in range(len(nums)):
            if target - nums[i] in D:
                return [D[target - nums[i]], i]
            D[nums[i]] = i
        
        return
# @lc code=end