class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans= []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 == 0:
                ans.insert( i,"FizzBuzz")
            elif i%3 == 0:
                ans.insert( i,"Fizz")
            elif i %5 ==0 :
                ans.insert( i,"Buzz")
            else:
                ans.insert(i,str(i)) 
        return ans
        


