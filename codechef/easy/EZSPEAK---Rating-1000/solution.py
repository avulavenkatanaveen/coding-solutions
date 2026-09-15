# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    v={'a','e','i','o','u'}
    consecutive_count=0
    is_easy=True
    for char in s:
        if char not in v:
            consecutive_count += 1
            if consecutive_count >= 4:
                is_easy = False
                break
                 
        else:
            consecutive_count = 0 
            
    if is_easy:
        print("YES")
    else:
        print("NO")
    