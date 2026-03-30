
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            print(f"Longitud {len(s)} es impar. Retornando False inmediatamente.")
            return False
            
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        print(f"{'Iteración':<10} | {'Carácter':<10} | {'Acción':<20} | {'Estado de la Pila'}")
        print("-" * 65)

        for i, char in enumerate(s):
            if char in bracket_map:
                # Caso: Es un cierre
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    print(f"{i+1:<10} | {char:<10} | ERROR: {char} no cierra {top_element} | {stack}")
                    return False
                print(f"{i+1:<10} | {char:<10} | Cierra {top_element:<13} | {stack}")
            else:
                # Caso: Es una apertura
                stack.append(char)
                print(f"{i+1:<10} | {char:<10} | Agregando a pila     | {stack}")

        # Si al final la pila está vacía, es válido
        final_valid = not stack
        print("-" * 65)
        print(f"Resultado Final: {'Válido' if final_valid else 'Inválido (Pila no vacía)'}")
        return final_valid

# Ejemplo de uso:
sol = Solution()
sol.isValid("([{}])")