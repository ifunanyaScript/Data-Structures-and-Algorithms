import time

def timely(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {str(round((end-start) * 1000, 5))} milli-seconds to execute.")
        return result
    return wrapper