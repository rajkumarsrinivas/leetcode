from typing import List

# this approach is from leetcode
def longestValidParentheses(s: str) -> int:
        left = right = maxlength = 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1

            if left == right:
                maxlength = max(maxlength, 2 * right)
            elif right >= left:
                left = right = 0;

        left = right = 0;
        for i in range(len(s)-1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2 * left)
            elif left >= right:
                left = right = 0;
        return maxlength

if __name__ == "__main__":
    print(longestValidParentheses("(()"))