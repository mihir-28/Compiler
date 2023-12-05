# Infix to postfix expresssion
def infix_to_postfix(expression):
    def precedence(operator):
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        return precedence.get(operator, 0)

    def is_operator(char):
        return char in "+-*/^"

    def is_higher_precedence(op1, op2):
        return precedence(op1) >= precedence(op2)

    postfix = []
    stack = []
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            if stack and stack[-1] == "(":
                stack.pop()
        elif is_operator(char):
            while stack and stack[-1] != "(" and is_higher_precedence(stack[-1], char):
                postfix.append(stack.pop())
            stack.append(char)
    while stack:
        postfix.append(stack.pop())

    return "".join(postfix)


# Example usage
infix_expression = "a*(b+c) - e/(f+g)"
# infix_expression = "y = (x*3) + (x*3)"
# infix_expression = "a + b * (c - d) / e"

postfix_expression = infix_to_postfix(infix_expression)
print(f"Infix Expression: {infix_expression}")
print(f"Postfix Expression: {postfix_expression}")
