# cook your dish here
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    if m>=n:
        print(n)
    else:
        e=n-m
        t=n+e
        print(t)