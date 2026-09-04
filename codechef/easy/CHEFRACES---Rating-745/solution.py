# cook your dish here
t=int(input())
for _ in range(t):
    x,y,a,b=map(int,input().split())
    m=0
    if x!=a and x!=b:
        m+=1
    if y!=a and y!=b:
        m+=1
    print(m)