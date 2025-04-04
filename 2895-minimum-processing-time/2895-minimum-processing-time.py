class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True) 
        n = len(processorTime)
        mx = 0
        for i in range(n):
            ps = processorTime[i]
            for j in range(4):
                task_index = 4 * i + j
                cp = ps + tasks[task_index]
                mx = max(mx, cp)
        
        return mx
        