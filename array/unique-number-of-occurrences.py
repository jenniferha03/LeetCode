class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
          hash = dict()
          for num in arr:
            if num in hash:
              hash[num] += 1
            else:
              hash[num] = 1

          vals = hash.values()

          if len(vals) != len(set(vals)):
            return False
          else:
            return True
        