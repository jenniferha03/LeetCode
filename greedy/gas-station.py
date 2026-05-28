class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)-sum(cost) < 0:
            return -1
        gasleft, total_gas = 0,0 
        start = 0
        for i in range(len(gas)):
            gasleft += gas[i] - cost[i]
            if gasleft >= 0:
                total_gas -= cost[i]
            else:
                start = i + 1
                total_gas, gasleft = 0, 0
        return start
            