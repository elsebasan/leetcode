import re

def validate_credit_card(text):
    #begin with 4, 5 o 6
    regex_begin = r"^[4-6].*"
    #it must contain exactly 16 digits or may have ditits in groups of 4 separated by one hyphen "-"
    regex_only_num_sep = r"^((\d{4}-\d{4}-\d{4}-\d{4})|(\d{16}))$"
    #I use to negate it must NOT have 4 or more consecutive repeated digits
    regex_repeated = r"(\d)\1{3,}"
    for line in text:
        if not re.search(regex_begin, line):
            print("Invalid")
        elif not re.search(regex_only_num_sep, line):
            print("Invalid")
        elif re.search(regex_repeated,''.join(filter(str.isdigit, line))):
            print("Invalid")
        else:
            print("Valid")

if __name__ == '__main__':
    n = int(input())
    text = []
    for i in range(n):
        text.append(input())
    validate_credit_card(text)
