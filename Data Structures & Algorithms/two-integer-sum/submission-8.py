class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hset = {}

       for i,n in enumerate(nums):
            diff = target - n
            if diff in hset:
                return [hset[diff],i]
            hset[n] = i