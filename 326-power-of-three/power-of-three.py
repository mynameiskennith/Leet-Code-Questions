class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        return n == 3** int(ceil(math.log(n,3)))