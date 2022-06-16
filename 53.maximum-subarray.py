#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSub = nums[0]
        curmax = 0
        for i in nums:
            if curmax < 0:
                curmax = 0
            
            curmax += i
            maxSub = max(curmax, maxSub)
        
        return maxSub
# @lc code=end

























        # 
        # maxSub = nums[0]
        # curmax = 0
        # for n in nums:
        #     if curmax < 0:
        #         curmax = 0
        #     curmax += n
        #     maxSub = max(maxSub, curmax)

        # return maxSub