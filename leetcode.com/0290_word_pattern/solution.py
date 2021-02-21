class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h = {}
        words = s.split(' ')
        
        if len(words) != len(pattern):
            return False
        
        p = iter(pattern)
        
        for word in words:
            try:
                pc =  next(p)    
            except StopIteration:
                return False
            
            if pc not in h.keys() and word in h.values():
                return False
            
            if h.get(pc, word) != word:
                return False

            h[pc] = word
        
        return True
