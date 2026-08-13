# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    
    a=y//x
    c=z-a
    d=max(0,c)
    print(d)
    