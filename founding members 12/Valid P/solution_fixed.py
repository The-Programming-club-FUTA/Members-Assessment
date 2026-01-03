def isValid(s: str) -> bool:
    open_brackets = {"(", "{", "["}
    stack = []

    for st in s:
        if st in open_brackets:
            stack.append(st)

    if len(stack) == 0:
        return False 
    
    if len(stack) % 2 != 0:
        return False

    for i in range(len(stack) // 2):
       if stack[i] != stack[len(stack) - 1 - i]:           return False

    return True
"""
this function loops through the string accepted as a parameter and adds them to a list in the order of a stack(first in last out).
it also checks if the input string length is even to make sure every opening parenthesis has a close.
it then checks if there's any string in the list, if none it returns false. if there's a string it then loops through the stack to check if the opening parenthesis matches or has a closing stbthe required index. 
"""
