# Problem: E - Zombie Invasion! - https://codeforces.com/gym/588094/problem/E

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    hp = list(map(int, input().split()))
    pos = list(map(int, input().split()))
    
    zombies = []
    for i in range(n):
        d = abs(pos[i])
        zombies.append((d, hp[i]))
    
    zombies.sort(key=lambda z: z[0])
    
    total = 0  
    possible = True
    for d, h in zombies:
        total += h
        if total > d * k:
            possible = False
            break
    
    print("YES" if possible else "NO")
