class Solution:
    def singleNumber(self, nums: List[int]) -> int:
          ans=0
        for num in nums:
            ans=ans^num
        return ans

'''class Solution:
    def singleNumber(nums):
        ans=0
        for num in nums:
            ans=ans^num
        return ans
        

if __name__=='__main__':
    print(Solution.singleNumber([4,1,2,1,2]))'''