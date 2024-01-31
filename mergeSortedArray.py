class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #finding the length of the nums1 to find the last character
        length = m + n - 1
        # m=m-1
        # n=n-1
        while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[length]=nums1[m-1]
                m-=1
            else:
                nums1[length]=nums2[n-1]
                n-=1
            length-=1

        while n>0:
            nums1[length]=nums2[n-1]
            n-=1
            length-=1

        return nums1     

        

var = Solution()
nums1=[1,2,1,0,0,0]
m=3
nums2=[2,5,6]
n=3
res=var.merge(nums1,m,nums2,n)
print(res)