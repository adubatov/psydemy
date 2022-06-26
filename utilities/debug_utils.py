from functools import wraps

def decorate(func):
    @wraps(func)
    def out(*args, **kwargs):
        print('=' * 30)
        func(*args, **kwargs)
        print('=' * 30)
    return out


