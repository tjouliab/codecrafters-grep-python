import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!

ALL_NUMBERS = [f'{i}' for i in range(10)]
ALL_LOWERCASE_LETTERS = [chr(i) for i in range(ord('a'), ord('z') + 1)]
ALL_UPPERCASE_LETTERS = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
ALL_ALPHANUMERIC_CHARACTERS = ALL_NUMBERS + ALL_LOWERCASE_LETTERS + ALL_UPPERCASE_LETTERS

def match_pattern(input_line: str, pattern: str) -> bool:
    subpatterns = extract_subpatterns(pattern)
    print('subpatterns', subpatterns)
    subpatterns_index = 0
    for input in input_line:
        print('input', input)
        subpattern = subpatterns[subpatterns_index]
        print('subpattern', subpattern)
        if not match_subpattern(input, subpattern):
            subpatterns_index = 0
        elif subpatterns_index + 1 == len(subpatterns):
            return True
        else:
            subpatterns_index += 1    
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

def extract_subpatterns(pattern: str) -> list[str]:
    subpatterns: list[str] = []
    pattern_blank_splitted = pattern.split(' ')
    for blank_split in pattern_blank_splitted:
        subpattern: list[str] = []
        index = 0
        while index < len(blank_split):
            if blank_split[index] == '\\':
                subpattern.append(blank_split[index : index + 2])
                index += 2
            elif blank_split[index] == '[':
                closing_bracket_index = blank_split.index(']', index)
                subpattern.append(blank_split[index : closing_bracket_index + 1])
                index = closing_bracket_index + 1
            else: 
                subpattern.append(blank_split[index])
                index += 1
        if len(subpatterns) >= 1:
            subpatterns += [' '] + subpattern
        else:
            subpatterns += subpattern
    return subpatterns

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
