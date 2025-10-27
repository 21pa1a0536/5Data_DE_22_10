def dec1(func):
    def wrap(*args, **kwargs):
        print("Decorator1 before Function Call")
        func(*args, **kwargs)
        print("Decorator1 after Function Call")
    return wrap

def dec2(func):
    def wrap(*args, **kwargs):
        print("Decorator2 before Function Call")
        func(*args, **kwargs)
        print("Decorator2 after Function Call")
    return wrap

def dec3(func):
    def wrap(*args, **kwargs):
        print("Decorator3 before Function Call")
        func(*args, **kwargs)
        print("Decorator3 after Function Call")
    return wrap


@dec1
@dec2
@dec3
def add(a,b):
    print(a+b)

add(3,7)

""" ORDER OF DECORATION: (((add(a,b)) wrapped by dec3) wrapped by dec2) wrapped by dec1 
                         i.e., starts at add() function and ends at dec1(outermost decorator).
                         Any New decorator wraps dec1.
                         add(a,b) -> dec3(add) -> dec2(dec3(add)) -> dec1(dec2(dec3(add)))

"""
"""ORDER OF EXECUTION:   first starts at outermost decorator(dec1) -> prints dec1 before function call, then goes to func (which is dec2(...) here)
                        then goes to dec2 -> prints dec2 before function call, then goes to func (which is dec3(add) here)
                        then goes to dec3 -> prints dec3 before function call, then goes to func (which is the original add function)
                        Runs add function, 
                        then Runs remaining dec3 part
                        then Runs remaining dec2 part
                        then Runs remaining dec1 part
"""