
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frecuencias = {} 
        for n in nums:
            if n in frecuencias:
                frecuencias[n] += 1 
            else:
                frecuencias[n] = 1  
        
        # Creamos una lista de [frecuencia, número] (al revés)
        lista_invertida = []
        for num, freq in frecuencias.items():
            lista_invertida.append([freq, num])

        # Ahora .sort() funciona perfecto porque la frecuencia está al inicio
        lista_invertida.sort(reverse=True)

        # Sacamos el número (que ahora está en la posición 1)
        resultado = []
        for i in range(k):
            resultado.append(lista_invertida[i][1])
            
        return resultado

#my_dict[i].append(value)
