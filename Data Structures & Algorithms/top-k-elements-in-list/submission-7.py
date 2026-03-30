#class Solution:
    #def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #my_dict = dict()
        #t1 = k
        #for i in nums:
            #counter = 0
            #for j in nums:
                #if i == j or counter == 0:
                    #counter += 1
                    #my_dict[j].append(counter)

#my_dict[i].append(value)

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 1. Contamos cuántas veces aparece cada número
        # Esto crea un diccionario como {num: frecuencia}
        counts = Counter(nums)
        
        # 2. Creamos "cubetas" (buckets)
        # El índice de la lista representa la frecuencia
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in counts.items():
            freq_buckets[freq].append(num)
            
        # 3. Recogemos los números de las cubetas empezando por la más alta
        res = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res