class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source_cities = set()
        for path in paths:
            source_cities.add(path[0])
        for path in paths:
            if path[1] not in source_cities:
                return path[1]
        