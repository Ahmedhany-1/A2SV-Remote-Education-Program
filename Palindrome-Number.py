1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        
4        if(x < 0):
5            return False
6        
7        n = x
8        ans = 0
9        while(n != 0):
10            ans *= 10
11            ans += n % 10
12            n = n // 10
13        return(ans == x)
14
15# 121
16# 121 
17
18        