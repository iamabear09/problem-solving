from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_result = []
        right_result = []
        result = []

        product = 1
        for i in range(0, len(nums)):
            left_result.append(product)
            product = product * nums[i]
        
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            right_result.append(product)
            product = product * nums[i]
        right_result.reverse()
        
        for i in range(len(nums)):
            result.append(left_result[i] * right_result[i])
        
        return result