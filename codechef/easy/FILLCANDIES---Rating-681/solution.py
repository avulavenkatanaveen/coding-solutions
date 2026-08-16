# cook your dish here
import math
t=int(input())
for _ in range(t):
    n,k,m=map(int,input().split())
    a=k*m
    print(math.ceil(n/a))
    
    