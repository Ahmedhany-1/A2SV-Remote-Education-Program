1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        ans = ""
4        first_str = strs[0]
5        last_str = strs[-1]
6        for i in range(min(len(first_str), len(last_str))):
7            if(first_str[i] != last_str[i]):
8                return ans
9            ans += first_str[i]
10        return ans
11
12
13
14
15