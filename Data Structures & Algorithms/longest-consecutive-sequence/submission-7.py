class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        my_list = list(my_set)
        my_list.sort()
        print(my_list)
        hits = 1
        highest_score = []
        for index in range(len(my_list)):
            if index + 1 < len(my_list):
                if  my_list[index] - my_list[index + 1] == -1:
                    hits += 1
                    print(hits)
                else:
                    highest_score.append(hits)
                    hits = 1
        highest_score.append(hits)
        highest_score.sort()
        if len(nums) > 0:
            return highest_score[-1]
        return 0

