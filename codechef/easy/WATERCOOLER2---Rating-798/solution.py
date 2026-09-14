# cook your dish here
import math
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if y>x:
        print((y-1)//x)
    else:
        print(0)
    