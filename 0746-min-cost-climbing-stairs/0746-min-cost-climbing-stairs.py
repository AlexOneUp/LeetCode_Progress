class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0] * len(cost)

        # Starting at the beginning index
        memo[0] = cost[0]
        # For any cost length beyond 2
        if len(cost) >= 2:
            memo[1] = cost[1]
        
        for i in range(2, len(cost)):
            memo[i] = cost[i] + min(memo[i-1], memo[i-2])
   
        return min(memo[-1] , memo[-2])

# T : O(1) + O(N - 2)
# S : O(N)