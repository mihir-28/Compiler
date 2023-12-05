# 3AC


def is_operator(char):
    return char in "+-*/"


def precedence(operator):
    if operator in "+-":
        return 1
    if operator in "*/":
        return 2
    return 0


def infix_to_postfix(expression):
    postfix = []
    operators = []

    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif is_operator(char):
            while (
                operators
                and is_operator(operators[-1])
                and precedence(operators[-1]) >= precedence(char)
            ):
                postfix.append(operators.pop())
            operators.append(char)
        elif char == "(":
            operators.append(char)
        elif char == ")":
            while operators and operators[-1] != "(":
                postfix.append(operators.pop())
            operators.pop()

    while operators:
        postfix.append(operators.pop())

    return "".join(postfix)


def generate_3ac(postfix):
    operands = []
    temp_count = 1
    code = []

    for char in postfix:
        if char.isalnum():
            operands.append(char)
        elif is_operator(char):
            right_operand = operands.pop()
            left_operand = operands.pop()
            result = f"t{temp_count}"
            temp_count += 1
            code.append(f"{result} = {left_operand} {char} {right_operand}")
            operands.append(result)

    return code


infix = "b * c + b * c / e"
postfix = infix_to_postfix(infix)
tac = generate_3ac(postfix)

print("postfix: ", postfix)
print("3AC:")
for line in tac:
    print(line)
