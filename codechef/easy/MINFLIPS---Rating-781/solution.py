# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if n%2!=0:
        print(-1)
    else:
        c=a.count(1)
        ans=abs(n//2-c)
        print(ans)