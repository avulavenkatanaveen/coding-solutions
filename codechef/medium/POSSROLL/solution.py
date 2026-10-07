# cook your dish here
x,k,y=map(int,input().split())
if y%k==0 and 1<=(y//k)<=x:
    print("YES")
else:
    print("NO")
