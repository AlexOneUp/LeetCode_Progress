class Solution:
    def isHappy(self, n: int) -> bool:
        sq_sum = sum([int(x) ** 2 for x in str(n)])
        n=sq_sum
        while n != 1: 
            sq_sum = sum([int(x) ** 2 for x in str(n)])
            if n == 4 :
                return False
            n = sq_sum
            print(sq_sum)
            
        # u can do the summation of x  ^ 2 for each char at string of n
        # sum(iterable, start)
        if len(str(n)) == 1 and n != 1:
            return False
        if len(str(n)) == 1 and n == 1:
            return True

"""


"""        