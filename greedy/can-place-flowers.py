class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flower = 0
        # bed[0] = 0 and n = 0 => True
        # bed[0] = 0 and n = 1 => True
        # bed[0] = 1 and n = 0 => True
        # bed[0] = 1 and n = 1 => False
        if len(flowerbed) == 1:
            return not (flowerbed[0] == 1 and n == 1)
        
        #Case 1: Flower plots at indices 0 and 1
        if (flowerbed[0] == 0 and flowerbed[1] == 0):
            flowerbed[0] = 1
            flower += 1
            
        for i in range(1, len(flowerbed)-1):
            #Case 2: Flower indices between 1 and n-2
            if (flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0):
                flowerbed[i] = 1
                flower += 1
        
        #Case 3: Flower plots at indices n-1 and n
        if (flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0):
            flowerbed[len(flowerbed)-1] = 1
            flower += 1
        
        return flower >= n
                
                