import re

def validate(text):
    regex1 = r"^(?!.*(.).*\1)[a-zA-Z\d]{10}$"
    regex_digit = r"(?:((.)*\d(.)*){3})"
    regex_upper = r"(?:((.)*[A-Z](.)*){2})"
    for line in text:
        if re.match(regex1, line) and re.match(regex_digit, line) and re.match(regex_upper, line):
            print("Valid")
        else:
            print("Invalid")



if __name__ == '__main__':
    n = int(input())
    text = []
    for i in range(n):
        text.append(input())
    validate(text)

