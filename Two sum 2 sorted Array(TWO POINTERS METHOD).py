class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f=0
        s=len(numbers)-1
        ans=[]
        
        
        while(f<s):
            cursum=numbers[f]+numbers[s]
            if (cursum <target):
                f=f+1
            elif (cursum>target):
                s=s-1
            else:
                ans.append(f+1)
                ans.append(s+1)
                break
        return ans
                
        
        
