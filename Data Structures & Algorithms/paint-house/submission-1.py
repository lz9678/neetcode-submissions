class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # dp[i][j] ith house, jth color: 0 red, 1 blue, 2 green
        n = len(costs)

        red = 0 # cost after painting red
        blue = 0 
        green = 0

        prev_red = costs[0][0]
        prev_blue = costs[0][1]
        prev_green = costs[0][2]

        for i in range(1, n):
            red = min(prev_blue, prev_green) + costs[i][0]
            blue = min(prev_red, prev_green) + costs[i][1]
            green = min(prev_red, prev_blue) + costs[i][2]

            prev_red, prev_blue, prev_green, = red, blue, green

        return min(prev_red, prev_blue, prev_green)  