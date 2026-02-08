1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False
5
6        arr = [0] * 26
7
8        for i in range(len(s)):
9            arr[ord(s[i]) - ord('a')] += 1
10            arr[ord(t[i]) - ord('a')] -= 1
11
12        for check in arr:
13            if check != 0:
14                return False
15        return True