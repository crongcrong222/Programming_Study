class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        answer = [0,0]
        if (len(nums) == 0):
            return [-1,-1]
        mid = (len(nums))//2
        if(len(nums) == 0):
            return [-1,-1]
        elif(nums[0]>target or nums[-1]<target):
            return [-1,-1]
        else:
            while(left<=right):
                if(target > nums[mid]):
                    left = mid + 1
                elif(target < nums[mid]):
                    right = mid -1
                else:
                    left = right = mid
                    while(left-1 >=0 and nums[left-1] == target):
                        left -=1
                    while(right + 1<=len(nums)-1 and nums[right+1] == target):
                        right +=1

                    return [left,right]

        return [-1,-1]