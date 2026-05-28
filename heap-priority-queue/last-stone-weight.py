class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while(len(stones)>1):
            top1 = stones.pop()
            top2 = stones.pop()
            if top1 != top2:
                top = top1-top2
                stones.append(top)
                stones.sort()
        if stones:
            return stones[0] 
        else:
            return 0
        
        