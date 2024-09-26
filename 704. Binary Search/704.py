## Binary Search with FOR loop on O(1) Complexity
def search(self, nums: List[int], target: int) -> int:
        left,mid = 0,0
        right = len(nums)-1

        for i in range((right//2+1)):
            mid = (left+right)//2
            if nums[left]== target:
                return(left)
            elif nums[right]== target:
                return(right)
 
            if nums[mid]== target:
                return(mid)
            else:
                if nums[mid]<target:
                    left = mid + 1
                else:
                    right = mid + 1
        return(-1)
