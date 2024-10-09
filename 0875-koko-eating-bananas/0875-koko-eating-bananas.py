class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()


        k = piles[len(piles) - 1]
        # print(piles)
        l, r = 1, k
        
        res = r
        while l <= r:
            k = (l + r) // 2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / k)
            
            if hrs <= h:
                res = min(res, k)
                r = k - 1
            else:    
                l = k + 1
        return res



'''
# Given arr of n piles
piles[i] = # bananas in a pile

Rate of banana eating = k
    Determine the min. # k to eat all piles of the arr of bananas
    If you finish a pile under k value, you cannot eat more bananas from piles


Example 1:
    for k = 1
    you would need 10 hours
    [1 // 1]    [4 // 1]    [3 // 1]    [2 // 2]
    1               4           3           2   = 10 hours needed

    total_hours < h

    for k = 2
    you would need 6 hours
    i.e [1] [4 // 2] [3 // 2] [2 // 2]
        1       2       2       1 = 6 hours

Example 2 :
'''

