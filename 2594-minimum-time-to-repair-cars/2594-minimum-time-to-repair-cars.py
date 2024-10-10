class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()
    
        # Bool function to see if cars can be repaired in lowest time
        def can_repair(t):
            res = 0
            for rank in ranks:
                res += int(math.sqrt(t//rank))
                
                if res >= cars:
                    return True
            return False

        # Binary search 
        
        l, r = 0, ranks[-1] * cars ** 2
        
        while l < r:
            mid = (l + r) // 2
            
            if can_repair(mid):
                r = mid
            else:
                l = mid + 1
        return r


'''
    ranks = array of mechanics with rank[i] = r
        -ranks will be length : 10^5
        
    ranks[i] = can repair N cars in r*N^2 mins  
        -ranks[i] will have at most 100 
        
    cars = total cars need to be repair
        -cars is 1 <= 10^6
        
    res = min time taken to repair all cars
    
    finding n
    n = floor((time/rank) ** 0.5)
    
    NOTE:  All mechanics can repair the cars simultaneously.
    
    

Ex :
ranks = [4, 2, 3, 1] 
cars = 10

ranks[0] = 4 * ?^2
ranks[1] = 2 * ?^2
ranks[2] = 3 * ?^2
ranks[3] = 1 * ?^2


Approach :
n = floor((time / r) ** 0.5)




''' 
        
        
