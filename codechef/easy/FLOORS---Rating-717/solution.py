# cook your dish here
import math
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    floor_x=math.ceil(x/10)
    floor_y=math.ceil(y/10)
    print(abs(floor_x-floor_y))