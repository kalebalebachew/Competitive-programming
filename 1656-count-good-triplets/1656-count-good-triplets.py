class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        triplet_count = 0
        n = len(arr)

        for i, val_i in enumerate(arr[:-2]):
            for j, val_j in enumerate(arr[i + 1:n - 1], start=i + 1):
                if abs(val_i - val_j) <= a:
                    for val_k in arr[j + 1:]:
                        if (
                            abs(val_j - val_k) <= b and
                            abs(val_i - val_k) <= c
                        ):
                            triplet_count += 1

        return triplet_count

