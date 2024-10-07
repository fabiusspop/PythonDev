# Why do we need decorators?

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t_start = time()
        result = fn(*args, **kwargs)
        t_end = time()
        print(f'It took {t_end - t_start} ms to finish.')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000):
        i * 5

long_time()