import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!

def match_pattern_recursive(input_line: str, pattern: str) -> bool:
    if len(pattern) == 0:
        return True
    elif pattern[:2] == '\\d':
        return input_line[0].isdigit() and match_pattern_recursive(input_line[1:], pattern[2:])
    elif pattern[:2] == '\\w':
        return input_line.isalnum() and match_pattern_recursive(input_line[1:], pattern[2:])
    elif pattern[0] == '[' and ']' in pattern:
        closing_bracket_index = pattern.index(']')
        chars = pattern[1 : closing_bracket_index]
        if pattern[1] == '^':
            return input_line[0] not in chars and match_pattern_recursive(input_line[1:], pattern[closing_bracket_index + 1:])
        return input_line[0] in chars and match_pattern_recursive(input_line[1:], pattern[closing_bracket_index + 1:])
    elif pattern[0] == '^':
        return match_pattern_recursive(input_line, pattern[1:])
    else:
        return pattern[0] == input_line[0] and match_pattern_recursive(input_line[1:], pattern[1:])

def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    if match_pattern_recursive(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()