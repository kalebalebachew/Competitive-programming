class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        l = defaultdict(int)
        w = set()
        l1 = []

        for winner, loser in matches:
            w.add(winner)
            l[loser] += 1

        for loser, c in l.items():
            if loser in w:
                w.remove(loser)
            if c == 1:
                l1.append(loser)

        return [sorted(list(w)), sorted(l1)]