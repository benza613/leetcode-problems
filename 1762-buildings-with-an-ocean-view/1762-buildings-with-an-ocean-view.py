class Solution:
    import collections;
    
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        result = deque([len(heights)-1])
        
        max_height = heights[-1]
        
        # to do len
        
        for b in range(len(heights)-2,-1, -1): 
            curr_build = heights[b]
            right_build = heights[b+1]
            
            if curr_build > right_build and curr_build > max_height:
                result.appendleft(b)
                
                max_height = curr_build
                
        return result
                
