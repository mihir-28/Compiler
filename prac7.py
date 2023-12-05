# Program to generate Code in abstract assembly language. Infinite no of registers assumed.


three_address_code = [
    ("t1", "=", "b", "+", "c"),
    ("t2", "=", "d", "-", "e"),
    ("t3", "=", "t1", "*", "t2"),
    ("a", "=", "t3", "", ""),
]
registers = {}
next_register = 0
operators = {
    "+": "ADD",
    "-": "SUB",
    "*": "MUL",
    "/": "DIV",
}
assembly_code = []

for instruction in three_address_code:
    result_variable, _, operand1, operator, operand2 = instruction

    if operand1 not in registers:
        registers[operand1] = f"R{next_register}"
        next_register += 1

    if operand2 not in registers:
        registers[operand2] = f"R{next_register}"
        next_register += 1

    result_register = f"R{next_register}"
    next_register += 1

    assembly_code.append(f"LOAD {operand1}, {registers[operand1]}")
    assembly_code.append(f"LOAD {operand2}, {registers[operand2]}")
    if operator:
        assembly_code.append(
            f"{operators[operator]} {registers[operand1]}, {registers[operand2]}, {result_register}"
        )
        assembly_code.append(f"STORE {result_register}, {result_variable}")

for instruction in assembly_code:
    print(instruction)
