# cook your dish here
t=int(input())
for _ in range(t):
    a,b,k=map(int,input().split())
    d=abs(a-b)
    s=(d+k-1)//k
    print(s)