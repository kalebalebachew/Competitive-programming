# Problem: B - Card Game - https://codeforces.com/gym/588094/problem/B

n = int(input())

cd = list(map(int, input().split()))

cards = [(value, i + 1) for i, value in enumerate(cd)]

cards.sort(key=lambda x: x[0])

for i in range(n // 2):
    print(cards[i][1], cards[-1 - i][1])