class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def find_root(node: int) -> int:
            if p[node] != node:
                p[node] = fr(p[node])
            return p[node]
      
        p = list(range(n))
      
        for start_node, end_node in edges:
            p[fr(start_node)] = fr(end_node)
      
        return fr(source) == fr(destination)