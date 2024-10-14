from collections import Counter, defaultdict, OrderedDict
import datetime
from time import time
from array import array

li = [1, 2, 3, 4, 5, 6, 7, 8]
print(Counter(li)) # this creates a counter object

sentence = 'blah blah blah bla bl b '
print(Counter(sentence))

dictionary = defaultdict(lambda: 'does not exist', {'a' : 1, 'b' : 2})
print(dictionary['a'])
print(dictionary['c'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d)

print(datetime.time())

print(datetime.time(5, 45, 2))

print(datetime.date.today())

arr = array('i', [1, 2, 3])
print(arr)

