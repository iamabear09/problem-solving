from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i, n in enumerate(nums):
            if target - n in nums[i + 1:]:
                result.append(i)
                result.append(nums[i+1:].index(target-n) + i + 1)
                
                break
        return result


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        # 키와 값을 바꿔서 딕셔너리로 저장
        # dictionary는 Hash Table을 사용하므로 조회 속도가 더 빠르다.
        for i, num in enumerate(nums):
            nums_map[num] = i
            
        for i, n in enumerate(nums):
            if target - n in nums_map and i != nums_map[target - n]:
                return [i, nums_map[target - n]]
        
        

#굳이 전부다 dictionary로 변경 후 메인 로직을 적용할 필요가 없다.
#메인 로직을 적용하면서 dictionary로 변경하면 된다.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i
            

        
