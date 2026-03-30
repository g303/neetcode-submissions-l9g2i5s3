class Solution:
    def isValid(self, s: str) -> bool:
        # Si la longitud es impar, es imposible que estén balanceados
        if len(s) % 2 != 0:
            return False
            
        # Mapa de cierre a apertura para una búsqueda rápida
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # Si es un carácter de cierre
            if char in bracket_map:
                # Sacamos el último elemento de la pila si no está vacía, 
                # de lo contrario usamos un valor "dummy" (#)
                top_element = stack.pop() if stack else '#'
                
                # Si el que sacamos no coincide con el que corresponde, es inválido
                if bracket_map[char] != top_element:
                    return False
            else:
                # Si es un carácter de apertura, lo metemos a la pila
                stack.append(char)

        # Al final, la pila debe estar vacía si todo se cerró correctamente
        return not stack
        