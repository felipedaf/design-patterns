"""
Singleton Design Pattern

Motivation:
 - For some components it only makes sense to have one in the system
 - E.g. the initializer call is expensive
 - Want to prevent anyone creating additional copies
 - Need to take care of lazy instantiation
"""

# Singleton Allocator

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls)\
                .__new__(cls, *args, **kwargs)

        return cls._instance


# Singleton Decorator

def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)

        return instances[class_]

    return get_instance


@singleton
class Database2:
    def __init__(self) -> None:
        print('Loading database')

if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)