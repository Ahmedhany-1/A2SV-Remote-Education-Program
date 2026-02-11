n = int(input())
s = input()

k = "ACTG"
ans = 1e9

for i in range(n - 3):
    cur = s[i:i+4]
    cur_score = 0
    for j in range(4):
        if cur[j] == k[j]:
            continue
        else:
            diff = abs(ord(cur[j]) - ord(k[j]))
            cur_score += min(diff, 26 - diff)
    ans = min(ans, cur_score)

print(ans)