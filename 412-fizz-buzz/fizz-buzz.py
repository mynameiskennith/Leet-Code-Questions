class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # list1=[]
        string = ''
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                string+=' FizzBuzz '
            else:
                if i%3==0:
                    string+=' Fizz '
                if i%5==0:
                    string+=' Buzz '
                if i%3!=0 and i%5!=0:
                    string+=f' {i} '
        return string.split()