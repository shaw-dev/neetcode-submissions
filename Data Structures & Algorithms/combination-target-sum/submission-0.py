class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        answer = []
        result =[]
        
        def dfs(idx, resultsum):

            if resultsum == target:
                answer.append(result.copy())
                return

            if resultsum>target:
                return
            if idx ==len(nums):
                # answer.append(result.copy())
            
                return
            
            result.append(nums[idx])
            dfs(idx, resultsum+nums[idx])
            result.pop()
            dfs(idx+1,resultsum)
        dfs(0,0)
        return answer

            