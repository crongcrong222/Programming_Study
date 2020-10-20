class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        for i in range(len(numbers)):
            tmp = numbers[left] + numbers[right]
            if(tmp<target):
                left+=1
            elif(tmp>target):
                right -=1
            elif(tmp == target):
                print(left,right)
                answer = [left+1,right+1]
                return answer