1class Solution:
2    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
3        count_loser = {}
4        players = set()
5        ans = [[], []]
6        for w,l in matches:
7            players.add(w)
8            players.add(l)
9            count_loser[l] = count_loser.get(l, 0) + 1
10
11        for p in players:
12            if count_loser.get(p,0) == 0:
13                ans[0].append(p)
14            elif count_loser.get(p) == 1:
15                ans[1].append(p)
16        
17        ans[0].sort()
18        ans[1].sort()
19        return ans