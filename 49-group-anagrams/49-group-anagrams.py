class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # input word --> identifier anagram --> put it in dict[id] => val[] <- append input word
        
        # { e: 1, a: 1, t: 1}
        
        groups = {}
        
        for word in strs:
            
            id_anagram = self.preprocess_word(word)
            
            if id_anagram in groups:
                groups[id_anagram].append(word)
            else:
                groups[id_anagram] = [word]
                
        
        result = []
        for k in groups:
            result.append(groups[k])
                
        return result
    
    # Alternate solution
    def groupAnagrams2(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
    
    def preprocess_word(self, s):
        return tuple(sorted(s))
        