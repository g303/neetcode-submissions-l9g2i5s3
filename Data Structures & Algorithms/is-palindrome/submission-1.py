import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        limpio = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return limpio == limpio[::-1]