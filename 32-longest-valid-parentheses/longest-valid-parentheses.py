class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = [-1]  # Base index for a valid substring
        longest = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    # This ')' cannot be matched.
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1])

        return longest
            