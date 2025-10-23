def add_multiply(a,b):
    c = a + b 
    d = c * 2
    print(d)
    return d 

def add_div(a,b):
    c  = add_multiply(a,b)
    e = c /2 
    print(e)

add_div(2,3)