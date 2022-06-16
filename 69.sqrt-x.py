#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 1, x
        while l <= r:
            mid = (l+r)//2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        
        return r
# @lc code=end


















        # case 1:
        # if x == 0:
        #     return 0
        # left, right = 1, x
        # while left <= right:
        #     mid = (left + right) // 2
        #     if mid * mid == x:
        #         return mid
        #     elif mid * mid < x:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return right