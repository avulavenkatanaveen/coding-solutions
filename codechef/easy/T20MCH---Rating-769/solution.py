# cook your dish here
r,o,c=map(int,input().split())
a=20-o
d=a*6
f=d*6
c=c+f
if c>r:
    print("YES")
else:
    print("NO")