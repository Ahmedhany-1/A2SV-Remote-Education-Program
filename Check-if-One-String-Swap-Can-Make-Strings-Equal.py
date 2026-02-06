1class Solution:
2    def areAlmostEqual(self, s1: str, s2: str) -> bool:
3        cnt = 0
4        if len(s1) != len(s2):
5            return False
6        
7        for i in range(len(s1)):
8            cnt += (s1[i] != s2[i])
9        s1 = sorted(s1)
10        s2 = sorted(s2)
11        return cnt <= 2 and s1 == s2
12        