from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        fixed = 0
        while fixed < len(nums) - 2:
            l, r = fixed + 1, len(nums) - 1
            while l < r:
                if nums[fixed] + nums[l] + nums[r] == 0:
                    result.append([nums[fixed], nums[l], nums[r]])
                    
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                    
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif nums[fixed] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
            fixed += 1
            while fixed < len(nums) - 2 and nums[fixed - 1] == nums[fixed]:
                fixed += 1
        return result


# 좀더 깔끔한 풀이
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    # 중복 예외 처리
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

        return results

