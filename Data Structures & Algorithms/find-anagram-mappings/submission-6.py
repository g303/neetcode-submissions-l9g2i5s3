class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output_list = []
        for i, n in enumerate(nums1):
            for j, k in enumerate(nums2):
                if n == k:
                    output_list.append(j)
                    break
        return output_list
