# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted((start, i) for i, (start, end) in enumerate(intervals))
        res = []
        for interval in intervals:
            end = interval[1] 
            idx = bisect.bisect_left(starts, (end,))
            if idx < len(starts):
                res.append(starts[idx][1])
            else:
                res.append(-1)

        return res