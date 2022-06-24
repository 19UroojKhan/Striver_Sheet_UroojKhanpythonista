class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        minimumsofar=prices[0]
        for i in range(1,len(prices)):
            curprofit=prices[i]-minimumsofar
            if curprofit>ans:
                ans=curprofit
            minimumsofar=min(minimumsofar,prices[i])
        return ans
        
        
'''class Solution:
    def maxProfit(prices):
        ans=0
        minimumsofar=prices[0]
        for i in range(1,len(prices)):
            curprofit=prices[i]-minimumsofar
            if curprofit>ans:
                ans=curprofit
            minimumsofar=min(minimumsofar,prices[i])
        return ans

if __name__=='__main__':
    print(Solution.maxProfit([7,1,5,3,6,4]))'''