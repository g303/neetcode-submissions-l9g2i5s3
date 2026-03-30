class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #my_dict = {}
        my_list = []
        for i, p in enumerate(heights):
            for j, l in enumerate(heights):
                bars = min(p,l)
                distancia = abs(i - j)
                val = bars * distancia
                #my_dict[(bars,distancia)] = val
                my_list.append(val)
        #ordenado = dict(sorted(my_dict.items(), key=lambda item: item[1]))
        #items =  list(ordenado.items())
        my_list.sort()
        #print(items[-1])
        #return items[-1][1]
        return my_list[-1]