class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        for p, s in pair:
            travelTime = (target - p) / s
            if not stack or travelTime > stack[-1]:
                stack.append(travelTime)
            travelTime = 0
        return len(stack)
