class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ordenado = sorted(s)
        t_ordenado = sorted(t)
        if s_ordenado == t_ordenado:
            return True
        else:
            return False

anagram_1 = Solution().isAnagram("racecar","carrace")
anagram_2 = Solution().isAnagram("jar","jam")
