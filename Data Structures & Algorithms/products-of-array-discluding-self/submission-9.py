class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lista_de_listas = []
        for k, v in enumerate(nums):
            nueva_lista = [x for i, x in enumerate(nums) if i != k] 
            product = 1
            for i in nueva_lista:
                product *= i
            lista_de_listas.append(product)
        
        return  lista_de_listas 


            