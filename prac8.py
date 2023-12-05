# Implementation of a basic expression evaluator that can handle binary operators (+, -, *, /), parentheses, and operator precedence.

precedence = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}
operator_stack = []
operand_stack = []


def apply_operator():
    operator = operator_stack.pop()
    operand2 = operand_stack.pop()
    operand1 = operand_stack.pop()
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        if operand2 != 0:
            result = operand1 / operand2
        else:
            raise ValueError("Division by zero")
    operand_stack.append(result)
    print(f"Apply operator: {operand1} {operator} {operand2} = {result}")


# Input expression
input_expression = "3 + 5 * 2 - ( 6 / 3 )"

tokens = input_expression.split()

for token in tokens:
    print(f"Token: {token}")
    if token.isnumeric():
        operand_stack.append(int(token))
        print(f"Push operand: {int(token)}")
    elif token in precedence:
        while (
            operator_stack
            and operator_stack[-1] in precedence
            and precedence[operator_stack[-1]] >= precedence[token]
        ):
            apply_operator()
        operator_stack.append(token)
        print(f"Push operator: {token}")
    elif token == "(":
        operator_stack.append(token)
        print(f"Push operator: {token}")
    elif token == ")":
        while operator_stack and operator_stack[-1] != "(":
            apply_operator()
        if operator_stack and operator_stack[-1] == "(":
            operator_stack.pop()
        print(f"Pop operators until (")

while operator_stack:
    apply_operator()

result = operand_stack[0]
print("Result:", result)
