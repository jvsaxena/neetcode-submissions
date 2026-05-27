class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        reverse_s = cleaned[::-1]
        return cleaned == reverse_s 
        