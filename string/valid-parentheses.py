class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                my_stack.append(i)
            elif (i == ")" or i == "}" or i == "]") and my_stack:
                if (i == ")" and my_stack[-1]=="(") or (i == "}" and my_stack[-1] == "{") or (i == "]" and my_stack[-1] == "["):
                    my_stack.pop()
                else:
                    return False
            else:
                return False
        return not my_stack
