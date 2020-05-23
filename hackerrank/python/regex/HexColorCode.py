import re

if __name__ == '__main__':
    n = int(input())
    text = ''
    for i in range(n):
        text+=input() + "\n"
    regex = r"(?<!^)(#(?:[\da-fA-F]{3}){1,2})"
    matches = re.finditer(regex, text, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        print(match.group())
