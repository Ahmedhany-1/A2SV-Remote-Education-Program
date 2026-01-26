1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        ans = ""
4        strs = sorted(strs)
5        first_str = strs[0]
6        last_str = strs[-1]
7        for i in range(min(len(first_str), len(last_str))):
8            if(first_str[i] != last_str[i]):
9                return ans
10            ans += first_str[i]
11        return ans
12
13
14
15
16