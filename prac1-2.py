# Tokenizer Scanner

import re

PREPROCESSOR_DIRECTIVE = "PREPROCESSOR_DIRECTIVE"
KEYWORD = "KEYWORD"
IDENTIFIER = "IDENTIFIER"
OPERATOR = "OPERATOR"
CONSTANT = "CONSTANT"
STRING_LITERAL = "STRING_LITERAL"
SPECIAL_SYMBOL = "SPECIAL_SYMBOL"
END_OF_FILE = "END_OF_FILE"

patterns = [
    (r"#\s*include\s*<.*?>", PREPROCESSOR_DIRECTIVE),
    (r"\b(int|char|if|else|while|for|return)\b", KEYWORD),
    (r"[a-zA-Z_][a-zA-Z0-9_]*", IDENTIFIER),
    (r"[-+*/%=()<>&|!]", OPERATOR),
    (r"\d+", CONSTANT),
    (r'"([^"\\]*(?:\\.[^"\\]*)*)"', STRING_LITERAL),
    (r"[{};,]", SPECIAL_SYMBOL),
]


def tokenize(program):
    tokens = []
    while program:
        for pattern, token_type in patterns:
            match = re.match(pattern, program)
            if match:
                lexeme = match.group(0)
                tokens.append((token_type, lexeme))
                program = program[len(lexeme) :].lstrip()
                break
        else:
            if program[0].isspace():
                program = program[1:]
            else:
                raise ValueError(f"Cannot tokenize: {program}")

    tokens.append((END_OF_FILE, "EOF"))
    return tokens


def main():
    program = """
    #include <stdio.h>
    int main() {
        int n, reversed = 0, remainder, original;
            printf("Enter an integer: ");
            scanf("%d", &n);
            original = n;

        while (n != 0) {
            remainder = n % 10;
            reversed = reversed * 10 + remainder;
            n /= 10;
        }

        if (original == reversed)
            printf("%d is a palindrome.", original);
        else
            printf("%d is not a palindrome.", original);

        return 0;
    }
    """
    print("Input Program:")
    print(program)
    print("\nTokens:")
    tokens = tokenize(program)
    for token_type, lexeme in tokens:
        print(f"Token: {lexeme}, Type: {token_type}")


if __name__ == "__main__":
    main()
