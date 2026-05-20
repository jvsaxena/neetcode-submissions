class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string += str(len(i)) + "#" + i
        return encoded_string


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # j will look for the "#" delimiter
            j = i
            while s[j] != "#":
                j += 1
            
            # Now j is at the "#". Everything from i to j is the length.
            length = int(s[i:j])
            
            # Extract the actual string using string slicing
            # Start right after the "#" (j + 1)
            # End after taking 'length' number of characters
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # Move i to the start of the next encoded block
            i = j + 1 + length
            
        return res
