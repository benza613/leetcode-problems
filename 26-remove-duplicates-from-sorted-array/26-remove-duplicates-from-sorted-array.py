class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        unique_list = [] 

        for x in nums: 
            if x not in unique_list: 
                unique_list.append(x)
                
        for idx, x in enumerate(unique_list):
            print(idx,len(unique_list) )
            if unique_list[idx] == nums[idx]:
                continue;
            
            swap_idx = nums.index(unique_list[idx])
            nums[idx] = nums[swap_idx]
            
        del nums[len(unique_list):]
        """
        
        nums[:]=list(OrderedDict.fromkeys(nums))
        return len(nums)
