t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    com={
        'A':'T',
        'T':'A',
        'C':'G',
        'G':'C'
    }
    ans=[]
    for char in s:
        ans.append(com[char])
    print("".join(ans))