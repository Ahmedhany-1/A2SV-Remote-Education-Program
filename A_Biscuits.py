t = int(input())
for _ in range(t):
    n = int(input())
    ans = n // 2
    if n % 2 == 0:
        ans -= 1
    print(ans)