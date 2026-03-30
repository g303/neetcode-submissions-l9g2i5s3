#class Solution:
#    def isValid(self, s: str) -> bool:
#        characters_dict = {
#            "(":")",
#            "{":"}",
#            "[":"]"
#            }
#        reverse_dict = {
#            ")":"(",
#            "}":"{",
#            "]":"["
#            }
#        len_s = len(s)
#        if len(s) % 2 != 0:
#            return False
#        for i in range(int(len(s)/2)):
#            if reverse_dict[s[i]] == characters_dict[s[len_s]]:
#                len_s -= 1
#            else:
#                return False
#        return True

class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            if char in bracket_map:
                # char is a closing bracket
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                # char is an opening bracket
                stack.append(char)
        
        # Valid if stack is empty (all brackets matched)
        return not stack

