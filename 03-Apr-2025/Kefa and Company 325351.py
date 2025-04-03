# Problem: Kefa and Company - https://codeforces.com/problemset/problem/580/B

n, d = map(int, input().split())
friends = []
for _ in range(n):
    m, s = map(int, input().split())
    friends.append((m, s))

friends.sort()
mx = 0
curr = 0
left = 0

for right in range(n):
    curr += friends[right][1]
    while friends[right][0] - friends[left][0] >= d:
        curr -= friends[left][1]
        left += 1
    mx = max(mx, curr)

print(mx)