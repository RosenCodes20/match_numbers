import re

nums = input()

my_regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

found_numbers = re.finditer(my_regex, nums)

for number in found_numbers:
    print(number.group(),end=" ")
