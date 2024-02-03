class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k]=nums[i] #this swaps the value(3) to the nonvalue(!3) in this case
                k+=1
        return k #its gonna return 2 because the loop is executed 2 times

var = Solution()
nums = [3,2,2,3]
val = 3
res=var.removeElement(nums,val)
print(res)