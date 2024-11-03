class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list1=[]
        for i in range(1,n+1):
            string = ''
            if i%3==0:
                string+='Fizz'
            if i%5==0:
                string+='Buzz'
            if i%3!=0 and i%5!=0:
                string=str(i)
            list1.append(string)
        return list1