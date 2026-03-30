class Solution:
    #def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #    my_list = []
    #    for index_i, val_i  in enumerate(numbers):
    #        for index_j, val_j in enumerate(numbers):
    #            if val_i + val_j == target and index_i < index_j and index_i != index_j:
    #                my_list.append(index_i + 1)
    #                my_list.append(index_j + 1)
    #                return my_list
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0                      # puntero al inicio
        right = len(numbers) - 1      # puntero al final

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # devolvemos índices 1-indexed
                return [left + 1, right + 1]

            elif current_sum < target:
                # la suma es muy pequeña → mover left hacia la derecha
                left += 1
            else:
                # la suma es muy grande → mover right hacia la izquierda
                right -= 1