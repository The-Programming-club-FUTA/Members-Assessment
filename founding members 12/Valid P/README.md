## Valid Parenthesis

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
 

### Example 1:

Input: `s = "()"`

Output: `true`

### Example 2:

Input: `s = "()[]{}"`

Output: `true`

### Example 3:

Input: `s = "(]"`

Output: `false`

### Example 4:

Input: `s = "([])"`

Output: `true`

### Example 5:

Input: `s = "([)]"`

Output: `false`

 

Constraints:

- `1 <= s.length <= 10^4`
- `s consists of parentheses only '()[]{}'.`



## Instruction

The `solution.py` file in this directory contains a buggy solution to this problem. Your task is to find and fix the bug in the solution. Please do not rewrite the entire solution. Create a new file named `solution_fixed.py`, copy the existing code from `solution.py` into it, and then apply your fix there.