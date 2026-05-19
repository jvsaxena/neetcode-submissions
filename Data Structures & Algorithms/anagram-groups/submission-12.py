class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
    
        for word in strs:
        # Sort the word to use as the dictionary key
            sorted_word = "".join(sorted(word))
        
        # If the sorted key is already in our dictionary, append the original word
            if sorted_word in words:
                words[sorted_word].append(word)
        # Otherwise, create a new key with a list containing the original word
            else:
                words[sorted_word] = [word]
            
    # The problem asks for a list of lists, which happens to be exactly the values of our dictionary
        return list(words.values())
            
