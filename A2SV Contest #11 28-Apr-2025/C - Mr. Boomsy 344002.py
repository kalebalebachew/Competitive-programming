# Problem: C - Mr. Boomsy - https://codeforces.com/gym/605795/problem/C

t = int(input())
for _ in range(t):
        s = input().strip()
        stack = []
        for ch in s:
            if ch == 'B' and stack and stack[-1] in ('A', 'B'):
                stack.pop()
            else:
                stack.append(ch)
        print(len(stack))
