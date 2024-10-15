import re

string = "Search this inside of this block of text."

# print('Search' in string)

pattern = re.compile('this')
a =  pattern.search(string)
print(a.group())

b = pattern.findall(string)
print(b)

c = pattern.fullmatch(string)
print(c)

d = pattern.match(string)
print(d)


# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())

# b = re.search('ths', string)
# print(b.group())