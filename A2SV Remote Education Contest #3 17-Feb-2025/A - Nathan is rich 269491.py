# Problem: A - Nathan is rich - https://codeforces.com/gym/588094/problem/A

t = int(input())

for _ in range(t):
    wheels = int(input())
    count = 0
    count += wheels // 4
    wheels = wheels % 4
    count += wheels // 2
    
    print(count)
        
    
    