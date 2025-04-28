# Problem: B - Aaron and Repeated Letters - https://codeforces.com/gym/605795/problem/B

n = input()
stack = []
for char in n:
    if stack and stack[-1] == char:
        stack.pop()
    else:
        stack.append(char)
print(''.join(stack))