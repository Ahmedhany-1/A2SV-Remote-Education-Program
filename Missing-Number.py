1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        x = sum(nums)
4        le = len(nums)
5        ans = (le * (le + 1) // 2) - x
6        return ans