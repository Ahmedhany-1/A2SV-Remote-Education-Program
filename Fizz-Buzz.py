1class Solution:
2    def fizzBuzz(self, n: int) -> List[str]:
3        ans = []
4        for i in range(1, n + 1):
5            if i % 3 == 0 and i % 5 == 0:
6                ans.append("FizzBuzz")
7            elif i % 3 == 0:
8                ans.append("Fizz")
9            elif i % 5 == 0:
10                ans.append("Buzz")
11            else:
12                ans.append(str(i))
13
14        return ans