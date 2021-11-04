"""
Decorator Design Pattern

Motivation:
 - Want to augment an object with additional fucntionality
 - Do not want rewrite or alter existing code (OCP)
 - Want to keep new functionality separate (SRP)
 - Need to be able to interact with existing structures
 - Two options:
"""
import time

def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'{func.__name} took {int((end - start) * 1000)}ms')
        return result
    
    return wrapper

def some_op():
    print('Starting op')
    time.sleep(1)
    print('We are done')
    return 123

if __name__ == '__main__':
    some_op()
    time_it(some_op)()