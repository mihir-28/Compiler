# Postfix Evaluation


def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in "+-*/":
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == "+":
                result = operand1 + operand2
            elif token == "-":
                result = operand1 - operand2
            elif token == "*":
                result = operand1 * operand2
            elif token == "/":
                if operand2 == 0:
                    raise ValueError("Division by zero")
                result = operand1 / operand2
            stack.append(result)
        print(f"Stack after token '{token}': {stack}")

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    return stack[0]


sample_expression = "23 4 5 * +"
result = evaluate_postfix(sample_expression)
print("Result of postfix evaluation:", result)
