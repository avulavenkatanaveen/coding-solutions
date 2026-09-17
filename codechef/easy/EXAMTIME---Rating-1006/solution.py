t = int(input())
for _ in range(t):
    d_dsa,d_toc,d_dm=map(int,input().split())
    s_dsa,s_toc,s_dm=map(int,input().split())
    d_total = d_dsa + d_toc + d_dm
    s_total = s_dsa + s_toc + s_dm
    
    if d_total>s_total:
        print("Dragon")
    elif d_total<s_total:
        print("Sloth")
    else:
        if d_dsa>s_dsa:
            print("Dragon")
        elif d_dsa<s_dsa:
            print("Sloth")
        else:
            if d_toc>s_toc:
                print("Dragon")
            elif d_toc<s_toc:
                print("Sloth")
            else:
                print("Tie")