1class Solution:
2    def finalValueAfterOperations(self, operations: List[str]) -> int:
3        x = 0
4        for i in range(len(operations)):
5            if '+' in operations[i]:
6                x += 1
7            else:
8                x -= 1
9        return x