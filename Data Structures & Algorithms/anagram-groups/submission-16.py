class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = dict()
        seen = set()
        for i in range(len(strs)):
            if strs[i] not in seen:
                my_dict[i] = []
                for value in strs:
                    if sorted(strs[i]) == sorted(value):
                        my_dict[i].append(value)
                        seen.add(value)
                                
        lista = list(my_dict.values())
        return lista
