# cook your dish here
t=int(input())
cum_p1=0
cum_p2=0
max_lead=0
winner=0
for _ in range(t):
    a,b=map(int,input().split())
    cum_p1+=a
    cum_p2+=b
    if cum_p1>cum_p2:
        cur_lead=cum_p1-cum_p2
        leader=1
    else:
        cur_lead=cum_p2-cum_p1
        leader=2
    if cur_lead>max_lead:
        max_lead=cur_lead
        winner=leader
print(winner,max_lead)
    