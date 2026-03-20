1class Solution:
2    def smallestNumber(self, num: int) -> int:
3        if num == 0:
4            return 0
5        elif num < 0:
6            num = -num
7            num = sorted(str(num), reverse = True)
8            num = int(''.join(num))
9            return -num
10        else:
11            num = str(num)
12            count = num.count('0')
13            num = sorted(num)
14            num = num[count:count+1] + ['0']*count + num[count+1:]
15            num = int(''.join(num))
16            return num