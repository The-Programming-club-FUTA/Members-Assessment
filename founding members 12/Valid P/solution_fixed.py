def isValid(s: str) -> bool:
    open_brackets = {"(", "{", "["}
    close_map = {")": "(", "}": "{", "]": "["}
    stack = []

    for st in s:
        if st in open_brackets:
            stack.append(st)
        elif st in close_map:
            if len(stack) == 0:
                return False
            if stack[-1] != close_map[st]:
                return False
            stack.pop()

    if len(stack) != 0:
        return False

    return True

"""
this function loops through the string accepted as a parameter and adds opening brackets to a list in the order of a stack (first in last out).
when a closing bracket is found, it checks if the stack is empty or if the top of the stack does not match the required opening bracket. if either fails it returns false.
if the top of the stack matches, it removes the opening bracket from the stack.
after looping through the string, if there are still items left in the stack it means some brackets were not closed, so it returns false.
if all checks pass and the stack is empty, it returns true meaning the string has valid parentheses.
"""
