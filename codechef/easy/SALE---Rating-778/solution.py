# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    d=min(a,b,c)
    e=a+b+c-d
    print(e)
    
