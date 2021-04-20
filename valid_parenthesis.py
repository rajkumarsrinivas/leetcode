#
# https://leetcode.com/problems/valid-parentheses/
#

from typing import List

def validParentheses(s: str) -> bool:
        result = False
        parenthesis = { "(" : ")" , "{" : "}", "[" : "]"}
        stack = []
        for a in list(s):
            if(len(stack) != 0 and parenthesis.get(stack[-1]) == a):
                stack.pop()
            else:
                stack.append(a)
        if(len(stack) == 0):
            result = True
        return result

if __name__ == "__main__":
    print(validParentheses("(()"))