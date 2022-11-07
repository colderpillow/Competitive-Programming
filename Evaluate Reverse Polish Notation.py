class Solution:
    def evalRPN(self, tokens):
        exp = ["+", "-", "*", "/"]
        stack = []
        for i in tokens:
            if i in exp:
                second_var = stack.pop()
                first_var = stack.pop()
                if i == "+":
                    res = first_var + second_var
                elif i == "-":
                    res = first_var - second_var
                elif i == "*":
                    res = first_var * second_var
                else:
                    res = int(first_var / second_var)

                stack.append(res)
            else:
                stack.append(int(i))
        ans = stack.pop()
        return ans
