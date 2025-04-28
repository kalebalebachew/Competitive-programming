# Problem: D - Electric Mayhem - https://codeforces.com/gym/605795/problem/D

s = input().strip()
n = len(s)
if n & 1:
    print("No")
    exit()

stack = []
for c in s:
    if stack and stack[-1] == c:
        stack.pop()
    else:
        stack.append(c)

print("Yes" if not stack else "No")
