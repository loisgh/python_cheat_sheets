import time

def timing_decorator(func):
    def custom_inner_function_name(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.4f} seconds to run")
        return result
    return custom_inner_function_name

@timing_decorator
def hello_world():
    print("Hello, World1!")
    time.sleep(5.0)
    print("Hello, World2!")


if __name__ == "__main__":
    hello_world()
