1class Solution:
2    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
3        freq = [0] * 52
4        for st,en in ranges:
5            freq[st] += 1
6            freq[en + 1] -= 1
7        
8        for i in range(1, len(freq)):
9            freq[i] += freq[i - 1]
10
11        for i in range(left, right + 1):
12            if(freq[i] == 0):
13                return False
14        
15        return True 
16        