import time

def timely(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution of {func.__name__} took {str(round((end-start) * 1000, 5))} milli-seconds")
        return result
    return wrapper