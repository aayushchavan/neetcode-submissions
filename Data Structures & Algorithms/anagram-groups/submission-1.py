class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        used = [False] * len(strs)  # Track which words we've already grouped
        
        for i in range(len(strs)):
            # Skip if we already grouped this word
            if used[i]:
                continue
            
            # Start a new group with this word
            current_group = [strs[i]]
            used[i] = True
            
            # Compare this word with every other word
            for j in range(i + 1, len(strs)):
                # Skip if already grouped
                if used[j]:
                    continue
                
                # Check if strs[i] and strs[j] are anagrams
                if self.areAnagrams(strs[i], strs[j]):
                    current_group.append(strs[j])
                    used[j] = True
            
            result.append(current_group)
        
        return result
    
    def areAnagrams(self, word1: str, word2: str) -> bool:
        # Different lengths = not anagrams
        if len(word1) != len(word2):
            return False
        
        # Count characters in word1
        for char in word1:
            # Count how many times this char appears in both words
            count1 = 0
            count2 = 0
            for c in word1:
                if c == char:
                    count1 += 1
            for c in word2:
                if c == char:
                    count2 += 1
            
            # If counts don't match, not anagrams
            if count1 != count2:
                return False
        
        return True