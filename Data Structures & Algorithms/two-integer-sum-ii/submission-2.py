class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_list = []
        for index_i, val_i  in enumerate(numbers):
            for index_j, val_j in enumerate(numbers):
                if val_i + val_j == target and index_i < index_j and index_i != index_j:
                    print (val_i, val_j)
                    my_list.append(index_i + 1)
                    my_list.append(index_j + 1)
                    return my_list