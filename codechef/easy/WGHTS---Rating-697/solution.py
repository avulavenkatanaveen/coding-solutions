# cook your dish here
t=int(input())
for _ in range(t):
    w,x,y,z=map(int,input().split())
    if w in (x,y,z,x+y,y+z,x+z,x+y+z):
        print("YES")
    else:
        print("NO")