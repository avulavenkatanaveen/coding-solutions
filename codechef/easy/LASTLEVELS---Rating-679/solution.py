# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    b=(x-1)//3
    t=x*y+b*z
    print(t)