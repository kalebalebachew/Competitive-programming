# Problem: C - Barking Password - https://codeforces.com/gym/588094/problem/C

p = input()
n = int(input())
barks = [input() for _ in range(n)]

  
if p in barks:
    print("YES")
else:
    found = False
    
    for fword in barks:
        for sword in barks:
            comb = fword + sword
            if p in comb:
                found = True
                break
        if found:
            break
        
    if found:
        print("YES")
    else:
        print("NO")

 
        