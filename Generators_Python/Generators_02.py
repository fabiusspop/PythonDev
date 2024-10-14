
# Remember that a list is an iterable.
# Generators --> are actually iterable.
#  BUT Not everything that is iterable is a generator. E.g.: list (iterable, but not generator)
# generators are a subset of iterables.

def generator_function(num):
    for i in range(num):
        yield i * 2

# for item in generator_function(10):
#     print(item)

g = generator_function(10)
print(g)

next(g)
next(g)

print(next(g))
print(next(g))