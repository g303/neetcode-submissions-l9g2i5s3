
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frecuencias = dict() # {}
        for n in nums:
            if n in frecuencias:
                frecuencias[n] += 1 
            else:
                frecuencias[n] = 1  
        print(frecuencias)
        lista_invertida = []
        for num, freq in frecuencias.items():
            lista_invertida.append([freq, num])
        
        print(lista_invertida)
        lista_invertida.sort(reverse=True)
        print(lista_invertida)

        resultado = []
        for i in range(k):
            resultado.append(lista_invertida[i][1])
            
        return resultado
