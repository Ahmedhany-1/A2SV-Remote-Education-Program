1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        mp = {}
4        for i,num in enumerate(nums):
5            x = target - num
6            if x in mp:
7                return[mp[x], i]
8            mp[num] = i