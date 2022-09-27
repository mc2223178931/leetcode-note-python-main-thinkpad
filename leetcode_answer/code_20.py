
class Solution:
    def __init__(self):
        self.left_str = ['(', '[', '{']

    """
        遍历字符串，左字符压入栈，右字符与栈顶匹配，则出栈，否则返回False。最后若栈为空，则返回True
    """
    def ismatch(self, char1, char2):
        if char1 not in self.left_str:
            return False
        else:
            if (char1 == '(' and char2 == ')') or (char1 == '[' and char2 == ']') or (char1 == '{' and char2 == '}'):
                return True
            else:
                return False
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 0:
            stack = []
            for i, symbol in enumerate(s):
                if symbol in self.left_str:
                    stack.append(symbol)
                else:
                    if len(stack) == 0:
                        return False
                    elif self.ismatch(stack[-1], symbol):
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0
        else:
            return False


if __name__ == "__main__":

    test = Solution()
    s1 = "()[]{}"
    status1 = test.isValid(s1)
    print(status1)

    s2 = "(]"
    status2 = test.isValid(s2)
    print(status2)

    s3 = "([{]})"
    status3 = test.isValid(s3)
    print(status3)

