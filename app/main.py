import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!

ALL_NUMBERS = [f'{i}' for i in range(10)]
ALL_LOWERCASE_LETTERS = [chr(i) for i in range(ord('a'), ord('z') + 1)]
ALL_UPPERCASE_LETTERS = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
ALL_ALPHANUMERIC_CHARACTERS = ALL_NUMBERS + ALL_LOWERCASE_LETTERS + ALL_UPPERCASE_LETTERS

def match_pattern(input_line: str, pattern: str) -> bool:
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern[:2] == '\\d':
        return find_characters_in_input_line(input_line, ALL_NUMBERS)
    elif pattern[:2] == '\\w':
        return find_characters_in_input_line(input_line, ALL_ALPHANUMERIC_CHARACTERS)
    elif pattern[0] == '[' and pattern[-1] == ']':
        if pattern[1] == '^':
            return not find_characters_in_input_line(input_line, pattern[2:-1])
        return find_characters_in_input_line(input_line, pattern[1:-1])
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def find_characters_in_input_line(input_line: str, characters: list[str]) -> bool:
    for input in input_line:
        if input in characters:
            return True
    return False

def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
