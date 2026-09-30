# cook your dish here
t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    lst=set(map(int,input().split()))
    r=[]
    for _ in range(k):
        seat=1
        while seat in r:
            seat+=1
            lst.add(seat)
            r.append(seat)
    print(*(r))