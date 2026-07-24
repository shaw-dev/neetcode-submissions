class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        answer=[]
        current =[]
        
        def solve( idx):

            if idx>=len(nums):
                answer.append(current.copy())
                return
            
            current.append(nums[idx])
            solve(idx+1)
            current.pop()
            solve(idx+1)
        solve(0)
        return answer

        

