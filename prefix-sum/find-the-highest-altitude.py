class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #altitude = [0]*(len(gain)+1) # O(N)
        max_alt, current_alt = 0, 0
        for amount in gain: # O(N)
            current_alt = amount + current_alt
            max_alt = current_alt if current_alt >= max_alt else max_alt
        return max_alt