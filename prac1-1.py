import re

# Define token types
PREPROCESSOR_DIRECTIVE = "PREPROCESSOR_DIRECTIVE"
KEYWORD = "KEYWORD"
IDENTIFIER = "IDENTIFIER"
OPERATOR = "OPERATOR"
CONSTANT = "CONSTANT"
STRING_LITERAL = "STRING_LITERAL"
SPECIAL_SYMBOL = "SPECIAL_SYMBOL"
END_OF_FILE = "END_OF_FILE"

# Regular expressions for token patterns
patterns = [
    (r"#\s*include\s*<.*?>", PREPROCESSOR_DIRECTIVE),
    (r"\b(int|char|if|else|while|for|return)\b", KEYWORD),
    (r"[a-zA-Z_][a-zA-Z0-9_]*", IDENTIFIER),
    (r"[-+*/%=()<>&|!]", OPERATOR),
    (r"\d+", CONSTANT),
    (r'"([^"\\]*(?:\\.[^"\\]*)*)"', STRING_LITERAL),
    (r"[{};,]", SPECIAL_SYMBOL),
]


# Function to tokenize the input program
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
            # Skip whitespaces and newlines
            if program[0].isspace():
                program = program[1:]
            else:
                raise ValueError(f"Cannot tokenize: {program}")
            # Add end of file token
    tokens.append((END_OF_FILE, "EOF"))
    return tokens


# Main function
def main():
    program = """
    #include <stdio.h>

    int factorial(int n) {
        if (n <= 1) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    int main() {
        int n = 5;
        int result = factorial(n);
        printf("Factorial of %d is %d\\n", n, result);
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
