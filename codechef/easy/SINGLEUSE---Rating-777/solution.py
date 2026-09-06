# cook your dish here
import math
t=int(input())
for _ in range(t):
    h,x,y=map(int,input().split())
    h=h-y
    a=1
    if h>0:
        a+=math.ceil(h/x)
    print(a)