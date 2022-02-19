class Solution:

    # https://leetcode.com/problems/beautiful-arrangement/
    
    def countArrangement(self, n: int) -> int:
        self.res = 0
        perms = [i for i in range(1, n+1)]
        
        # recursively check if that particular combination 
        def checkPerm(nums: list, i: int = 1):
            if i == n+1: 
                self.res += 1
                return
            
            for j, num in enumerate(nums):
                if not(num % i and i % num):
                    checkPerm(nums[:j] + nums[j+1:], i+1)
            
        checkPerm(perms)
        return self.res


x = Solution()

print(x.countArrangement(1))
print(x.countArrangement(2))
print(x.countArrangement(5))