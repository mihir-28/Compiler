# First-Follow


def compute_first(grammar):
    first = {}
    non_terminals = set()

    for non_terminal, derivations in grammar.items():
        non_terminals.add(non_terminal)
        first[non_terminal] = set()

    def compute_first_recursive(derivation, first_set):
        if derivation and derivation[0] in non_terminals:
            for symbol in grammar[derivation[0]]:
                compute_first_recursive(symbol + derivation[1:], first_set)
        elif derivation:
            first_set.add(derivation[0])

    for non_terminal in non_terminals:
        for derivation in grammar[non_terminal]:
            compute_first_recursive(derivation, first[non_terminal])

    return first


def compute_follow(grammar, start_symbol):
    follow = {}
    non_terminals = set()

    for non_terminal, derivations in grammar.items():
        non_terminals.add(non_terminal)
        follow[non_terminal] = set()
    follow[start_symbol] = {"$"}

    def compute_follow_recursive(derivation, follow_set):
        if derivation and derivation[0] in non_terminals:
            for symbol in grammar[derivation[0]]:
                compute_follow_recursive(symbol + derivation[1:], follow_set)
        elif derivation:
            follow_set.add(derivation[0])

    for non_terminal in non_terminals:
        for production in grammar:
            for derivation in grammar[production]:
                if non_terminal in derivation:
                    idx = derivation.index(non_terminal)
                    if idx < len(derivation) - 1:
                        compute_follow_recursive(
                            derivation[idx + 1 :], follow[non_terminal]
                        )
                    if (
                        idx == len(derivation) - 1
                        or derivation[idx + 1] in follow[non_terminal]
                    ):
                        follow[non_terminal] |= follow[production]

    return follow


# Example usage
# grammar = {
#     "S": ["aAb", "bBa", "c"],
#     "A": ["aA", ""],
#     "B": ["bB", ""],
# }

# grammar = {
#     "S": ["ACB", "CbB", "Ba"],
#     "A": ["da", "BC"],
#     "B": ["g", ""],
#     "C": ["h", ""]
# }

grammar = {
    "S": ["aBDh"],
    "B": ["cC"],
    "C": ["bC", ""],
    "D": ["EF"],
    "E": ["g", ""],
    "F": ["f", ""],
}

start_symbol = "S"
first = compute_first(grammar)
follow = compute_follow(grammar, start_symbol)

print("FIRST sets:")
for non_terminal, first_set in first.items():
    print(f"FIRST({non_terminal}) = {first_set}")

print("\nFOLLOW sets:")
for non_terminal, follow_set in follow.items():
    print(f"FOLLOW({non_terminal}) = {follow_set}")
