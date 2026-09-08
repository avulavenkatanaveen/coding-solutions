# cook your dish here
import math
t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    n=int(math.log2(n))
    a=n*a
    b=(n-1)*b
    print(a+b)
    