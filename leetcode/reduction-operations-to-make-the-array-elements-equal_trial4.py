class Solution:
    def reductionOperations(self, a: List[int]) -> int:
        return sum(i*gt(*p) for i,p in enumerate(pairwise(sorted(a)[::-1]),1))