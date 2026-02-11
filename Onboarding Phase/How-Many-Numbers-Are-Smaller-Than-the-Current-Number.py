1class Solution:
2    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
3        nums2 = sorted(nums)
4        mp = {}
5
6        for i, num in enumerate(nums2):
7            if num not in mp:
8                mp[num] = i
9        
10        return [mp[num] for num in nums]