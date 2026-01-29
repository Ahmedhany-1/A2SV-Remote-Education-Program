1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        sz = len(nums)
4        mp = {}
5        for num in nums:
6            mp[num] = mp.get(num, 0) + 1
7        for num,freq in mp.items():
8            if(freq > sz // 2):
9                return num