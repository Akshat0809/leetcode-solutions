class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n 
        
        if k == 0:
            return
        
        def reverse(start,end):
            while(start<end):
                nums[start],nums[end] = nums[end],nums[start]
                start+=1
                end-=1

        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)

        # left,right = 0,len(nums)-1
        # while(left<right):
        #     nums[left],nums[right] = nums[right],nums[left]
        #     left+=1
        #     right-=1
        
        # left,mid1 = 0,k-1
        # mid2,right = k,len(nums)-1

        # while(left<mid1):
        #     nums[left],nums[mid1] = nums[mid1],nums[left]
        #     left+=1
        #     mid1-=1

        # while(mid2<right):
        #     nums[mid2],nums[right] = nums[right],nums[mid2]
        #     mid2+=1
        #     right-=1