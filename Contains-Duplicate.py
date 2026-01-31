1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        n = len(nums)
4        st = set(nums)
5        return n != len(st)
6