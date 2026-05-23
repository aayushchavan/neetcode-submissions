class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hset = {}
        
        for i, v in enumerate(nums):
            diff = target - v
            if diff in hset:
                return [hset[diff],i]
            else:
                hset[v] = i
