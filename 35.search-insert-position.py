#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return l
# @lc code=end





























        # Case 1:
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     nums.append(target)
        #     nums.sort()
        #     return nums.index(target)
        
        # Case2:
        # Log(n)
        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     mid = (l + r) // 2
        #     if target == nums[mid]:
        #         return mid
        #     if target > nums[mid]:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        
        # return l