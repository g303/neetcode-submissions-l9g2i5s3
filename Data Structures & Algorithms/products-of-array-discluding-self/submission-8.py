class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lista_de_listas = []
        for k, v in enumerate(nums):
            nueva_lista = [x for i, x in enumerate(nums) if i != k] 
            lista_de_listas.append(nueva_lista)
        
        final_list = []
        for sub_lista in lista_de_listas:
            product = 1
            for elemento in sub_lista:
                product *= elemento
            final_list.append(product)
   
        print(lista_de_listas)
        return  final_list 


            