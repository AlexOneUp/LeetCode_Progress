class Solution:
    def isHappy(self, n: int) -> bool:

        while n != 1: 
            """
                u can do the summation of x  ^ 2 for each char at string of n
                sum(iterable, start)
            """ 
            sq_sum = sum([int(x) ** 2 for x in str(n)])
            # Magic Math property https://en.wikipedia.org/wiki/Happy_number
            if n == 4 :
                return False
            n = sq_sum
            print(sq_sum)
         
        if len(str(n)) == 1 and n == 1:
            return True
   



"""


"""        