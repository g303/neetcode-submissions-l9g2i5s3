class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ordenado = "".join(sorted(s))
        t_ordenado = "".join(sorted(t))
        if s_ordenado == t_ordenado:
            return True
        else:
            return False

var_1 = Solution().isAnagram("racecar","carrace")
var_2 = Solution().isAnagram("jar","jam")
