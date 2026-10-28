class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0 
        right = len(numbers) - 1
        index1,index2 = 0,0
        ans = []
        while(left < right):
            if(numbers[left]+numbers[right] == target):
                index1 = left
                index2 = right
                ans.append(left+1)
                ans.append(right+1)
                break
            else:
                if(numbers[left]+numbers[right] > target):
                    right -= 1
                else:
                    left += 1
        return ans