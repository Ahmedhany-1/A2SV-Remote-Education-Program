1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        n = len(nums)
4        if(n == 1):
5            return False
6
7        nums = sorted(nums)
8        
9        j = 1
10        for i in range(n):
11            if(j < n  and nums[i] == nums[j]):
12                return True
13            j += 1
14        return  False
15