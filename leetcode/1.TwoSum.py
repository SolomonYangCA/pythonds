#!/usr/bin/env python

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # error
        _len = len(nums)
        if _len < 2:
            return [-1, -1]

        # sort list of nums, O(LogN)
        _nums = sorted(nums)

        # 2 pointers, left and right
        left = 0
        right = _len - 1

        while left < right:
            sum = _nums[left] + _nums[right]

            # get result
            if sum == target:
                _left = nums.index(_nums[left])
                if _nums[left] == _nums[right]: 
                    _right = nums.index(_nums[right], _left+1) 
                else:
                    _right = nums.index(_nums[right])
                return [_left, _right]

            # if sum > target, move left+1, otherwise, right-1
            if sum > target:
                right -= 1
            else:
                left += 1

        # reach here, means no solution
        return [-1, -1]

if __name__ == "__main__":
    print Solution().twoSum([3,2,4], 6)
    print Solution().twoSum([3,22,2,234,45,33,4,5,4], 50)
    print Solution().twoSum([-1,-2,-3,-4,-5], -8)
