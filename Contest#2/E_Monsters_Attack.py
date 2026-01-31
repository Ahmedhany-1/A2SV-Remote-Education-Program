t = int(input())
for t in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))

    mp = dict()

    for i in range(n):
        pos = abs(x[i])
        if pos in mp:
            mp[pos] += a[i]
        else:
            mp[pos] = a[i]

    total = 0
    helth_we_need = 0
    f = True
    mp_sorted = sorted(mp.items())

    for pos, helth in mp_sorted:
        helth_we_need += helth
        max_k = k * pos 

        if helth_we_need > max_k:
            print("NO")
            f = False
            break
    if f:
        print("YES")
    
    # print(mp)