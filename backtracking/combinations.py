class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combi = []
        ans = []
        idx = 0

        def backtrack(index: int, k: int, combi_arr: List[int]):
            if k == 0:
                ans.append(combi_arr[:])
                return			

            for i in range(index+1,n+1):
                combi_arr.append(i) 
                backtrack(i, k-1, combi_arr)
                combi_arr.pop()
                

        backtrack(idx, k, combi) 
        return ans