import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!

ALL_NUMBERS = [f'{i}' for i in range(10)]
ALL_LOWERCASE_LETTERS = [chr(i) for i in range(ord('a'), ord('z') + 1)]
ALL_UPPERCASE_LETTERS = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
ALL_ALPHANUMERIC_CHARACTERS = ALL_NUMBERS + ALL_LOWERCASE_LETTERS + ALL_UPPERCASE_LETTERS

def match_pattern(input_line: str, pattern: str) -> bool:
    pattern_index = 0
    for input in input_line:
        print('input', input)
        if pattern[pattern_index] == '\\':
            subpattern = pattern[pattern_index : pattern_index + 2]
            pattern_index += 2
        elif pattern[pattern_index] == '[':
            closing_bracket_index = pattern.index(']', pattern_index)
            subpattern = pattern[pattern_index : closing_bracket_index + 1]
        else:
            subpattern = pattern[pattern_index]
            pattern_index += 1
        print('subpattern', subpattern)
        if not match_subpattern(input, subpattern):
            pattern_index = 0
        elif pattern_index == len(pattern):
            return True
    return False

def match_subpattern(input_line: str, subpattern: str) -> bool:
    if len(subpattern) == 1:
        return subpattern in input_line
    elif subpattern[:2] == '\\d':
        return find_characters_in_input_line(input_line, ALL_NUMBERS)
    elif subpattern[:2] == '\\w':
        return find_characters_in_input_line(input_line, ALL_ALPHANUMERIC_CHARACTERS)
    elif subpattern[0] == '[' and subpattern[-1] == ']':
        if subpattern[1] == '^':
            return not find_characters_in_input_line(input_line, subpattern[2:-1])
        return find_characters_in_input_line(input_line, subpattern[1:-1])
    else:
        raise RuntimeError(f"Unhandled subpattern: {subpattern}")


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
