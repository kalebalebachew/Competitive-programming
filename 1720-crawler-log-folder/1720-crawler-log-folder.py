class Solution:
    def minOperations(self, logs: List[str]) -> int:
        zstack = []
        for log in logs:
            if log  == '../':
                if zstack:
                    zstack.pop()
            elif log != '../' and log != './':
                zstack.append(log)
        return len(zstack)
        