from constants import UNKNOWN_COMMAND


def access_control(attrname, value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if args and hasattr(args[0], attrname) and getattr(args[0], attrname) == value:
                result = func(*args, **kwargs)
                return result
            else:
                print(UNKNOWN_COMMAND)
        return wrapper
    return decorator
