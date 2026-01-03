def isValid(s: str) -> bool:
    open_brackets = {"(", "{", "["}
    stack = []

    for st in s:
        if st in open_brackets:
            stack.append(st)
      
    if not stack \
       or (stack[0] == "(" and stack[-1] != ")") \
       or (stack[0] == "{" and stack[-1] != "}") \
       or (stack[0] == "[" and stack[-1] != "]") \
       :
       return False
            
      stack.pop()

    return True
"""
this function loops through the string accepted as a parameter and adds them to a list in the order of a stack(first in last out).
it then checks if there's any string in the list, if none it returns false. if there's a string it then checks for 
"""
