class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # count the appearances of each elem
        vals = Counter(nums)
        # there must always be at least 1 subset in the nums
        res = 1
        
        
        for k in vals:
            
            # edge case for dealing with 1s
            # to build a pyramid, you have to have a odd # of numbers
            if k == 1:
                res = max(res, vals[1] if vals[1] % 2 else vals[1] - 1)
                continue
            
            #core logic
            # the peak of a subset x^k
            
            #for every single key, does a squared key exist?
            square_k = k **2
            
            #if it does and there's more than 1 key, then that's not the best solution
            if vals[k] > 1 and square_k in vals:
                continue
            # when you get to valid top of the pyramid 
            # count is 1 and keep trying to sq root
            count = 1
            curr = k ** 0.5 
            
            while curr in vals and vals[curr] >= 2:
                count+=2
                curr = curr**(0.5)
            res = max(res, count)
        return res
            
        
        
        
'''
positive integers nums

subset nums:
- place selected elements in 0-indexed array
    -follows pattern
        - [x, x2, x4, ..., x^k/2, x^k, x^k/2, ..., x4, x2, x]
    - k can be non-neg power of 2:
        - (2,4,16,4,2 )
        - (3, 9, 3)
        X (2, 4, 8, 4, 2)

returns MAX # elements in subset above conds

Intuition:
- 1. we can look at each individual element in O(n) time and look for the next powers that satisfy the conditions

- 1. conversely, we can look at sq. root of the element and see if it exists inside the list, if it does, then we can start building out the subsets
    -2. Find the peak and the sq root
    -3. The sq root of the peak will look like this
        i.e [2,2,2,2,4,4,4,4,16,16,16^2]
        16^2
       16  16
        4   4
        2  2
        whereby, 1+2+2+2 = 7 
{
16^2:1
16:2
4:4
2:4
}

    KEY INTUITION :
        - Always check for valid top which is a square of a # in the hashmap
            - and is only 1
    

'''