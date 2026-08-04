class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,v in enumerate(nums):
            compliment=target-v
            if compliment in seen:
                result = [seen[compliment],i]  
            else:
                seen[v]=i     
        return result
        