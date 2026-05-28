class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(nums, search_first):
            pos = -1
            l, r = 0, len(nums)-1
            while l <= r: 
                mid = (l + r) // 2
                if nums[mid] == target:
                    pos = mid
                    if search_first:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return pos

        first = find_bound(nums, search_first=True)
        last = find_bound(nums, search_first=False)

        return [first, last]