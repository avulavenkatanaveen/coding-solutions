# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    a=(500-2*x)+(1000-4*(x+y))
    b=(1000-4*y)+(500-2*(x+y))
    print(max(a,b))
    