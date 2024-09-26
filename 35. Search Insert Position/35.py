 def searchInsert(self, nums: List[int], target: int) -> int:
        
        left,mid,exp = 0,0,0
        right = len(nums)-1
        if target > nums[right]:
            return(right+1)
        elif target < nums[left]:
            return(left)
            print(a)
        for i in range((right//2)+1):
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
                    exp = mid -1
        if nums[mid] < target:
            return(mid+1)
        return(mid)
