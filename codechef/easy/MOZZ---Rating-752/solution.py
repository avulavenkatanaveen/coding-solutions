# cook your dish here
import math
t=int(input())
for _ in range(t):
    x,y,r=map(int,input().split())
    r=r//30
    c=x+r
    d=math.ceil(c/y)
    print(d)