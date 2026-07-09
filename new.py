
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before running")
        func(*args, **kwargs)
        print("After running")
    return wrapper

@decorator
def add(a, b):
    print(a + b)

add(3, 8)
