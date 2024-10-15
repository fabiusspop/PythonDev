import re

pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")

password = "safaffsa3132$nfa9" # has to end in a digit

check = pattern.fullmatch(password)

print(check)