# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = int(input())
a = list(map(int, input().split()))
has_odd = any(x % 2 for x in a)
has_even = any(x % 2 == 0 for x in a)
if has_odd and has_even:
    a.sort()
print(*a)
