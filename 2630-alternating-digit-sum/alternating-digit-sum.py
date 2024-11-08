class Solution:
    def alternateDigitSum(self, n: int) -> int:
        num = str(n)
        e = True
        s=0
        for i in num:
            if e:
                s+=int(i)
                e = False
            else:
                s+= -int(i)
                e= True
        return s