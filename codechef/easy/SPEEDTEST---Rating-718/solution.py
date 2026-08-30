# cook your dish here
t = int(input())
for _ in range(t):
    d1, f1, d2, f2 = map(int, input().split())
    
    alice_val = d1 * f2
    bob_val = d2 * f1
    
    if alice_val > bob_val:
        print("ALICE")
    elif bob_val > alice_val:
        print("BOB")
    else:
        print("EQUAL")