class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #s_ordenado = sorted(s)
        #t_ordenado = sorted(t)
        #if s_ordenado == t_ordenado:
        #    return True
        #else:
        #    return False
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

anagram_1 = Solution().isAnagram("racecar","carrace")
anagram_2 = Solution().isAnagram("jar","jam")
