import time
from functools import wraps

def retry_on_exception(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Exception caught: {e}")
                    print(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                    attempt += 1
            else:
                raise RuntimeError(f"Failed after {max_retries} attempts")

        return wrapper

    return decorator

# # Example usage:
# @retry_on_exception(max_retries=5, delay=2)
# def example_function():
#     # Replace this with the function you want to retry
#     return 1 / 0  # This will raise a ZeroDivisionError

# # Testing the decorated function
# try:
#     result = example_function()
#     print(f"Function returned: {result}")
# except RuntimeError as e:
#     print(f"Function failed: {e}")
