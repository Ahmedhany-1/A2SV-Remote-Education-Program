t = int(input())
for _ in range(t):
    k = 5;
    a,b,c = map(int, input().split())
    while(k > 0):
        if(a <= b and a <= c):
            a += 1
        elif(b < a and b < c):
            b += 1
        else:
            c += 1
        k -= 1
    print(a * b * c)
