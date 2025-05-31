import threading


def log_thread_async(func):
    async def wrapper(*args, **kwargs):
        print(f"Async function {func.__name__} started in thread: {threading.current_thread().name}")
        result = await func(*args, **kwargs)
        print(f"Async function {func.__name__} finished in thread: {threading.current_thread().name}")
        return result

    return wrapper


def call_logging(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper
