#
# https://leetcode.com/problems/longest-valid-parentheses/
#

from typing import List

# this approach is by me. I used 2 stack.. but this can be done using one stack as well..
def longestValidParentheses(s: str) -> int:
        parenthesis = { "(" : ")"}
        arr = list(s)
        stack = []
        stack_pos = [-1]
        max = 0
        for i, a in enumerate(list(s)):
            if(len(stack) != 0 and parenthesis.get(stack[-1]) == a):
                stack.pop()
                stack_pos.pop()
                if((i-stack_pos[-1]) > max):
                        if(len(stack_pos)==0):
                                max += i-stack_pos[-1]
                        else:
                                max = i-stack_pos[-1]
            else:
                stack.append(a)
                stack_pos.append(i)
        return max

if __name__ == "__main__":
    print(longestValidParentheses("()(()))())())"))