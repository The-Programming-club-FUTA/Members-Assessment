def isValid(s: str) -> bool:
    open_brackets = {"(", "{", "["}
    stack = []

    for st in s:
        if st in open_brackets:
            stack.append(st)
        else:
            if not stack \
                or (st == ")" and stack[-1] != "(") \
                or (st == "}" and stack[-1] != "{") \
                or (st == "]" and stack[-1] != "[") \
                :
                return False
            
            stack.pop()

    return True
