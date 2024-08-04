# The best solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0

        for n in nums:
            res = res ^ n
        return res

# My Solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        s=0
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in nums:
            if dic[i]==1:
                s=i
        return s

# Same method different answer
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)

        for n,c in count.items():
            if c==1:
                return n