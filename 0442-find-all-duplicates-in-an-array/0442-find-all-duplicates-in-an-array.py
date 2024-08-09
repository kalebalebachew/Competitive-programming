class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        k={}
        n =[]
        for i in nums:
            if(i not in k):
                k[i]=1
            else:
                n.append(i)

        return n