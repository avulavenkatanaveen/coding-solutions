# cook your dish here
import math
t=int(input())
for _ in range(t):
    x,n=map(int,input().split())
    p=math.ceil(n/100)
    ans=max(0,p-x)
    print(ans)