class Solution:
    def alternateDigitSum(self, n: int) -> int:
        num = str(n)
        return sum(int(num[i]) if i % 2 == 0 else -int(num[i]) for i in range(len(num)))

        # e = True
        # s=0
        # for i in num:
        #     if e:
        #         s+=int(i)
        #         e = False
        #     else:
        #         s+= -int(i)
        #         e= True
        # return s