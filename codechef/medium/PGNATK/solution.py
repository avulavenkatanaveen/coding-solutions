# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    ans=n+(n-1)//(k-1)
    print(ans)