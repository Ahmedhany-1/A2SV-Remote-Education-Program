k,w,n = map(int, input().split())

total = k * (n * (n + 1) // 2)


print(max(0, total - w))

