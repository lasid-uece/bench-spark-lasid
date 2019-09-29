import sys


def mstos(x):
    val = x/1000
    return val
      
def ustos(x):
    val = x/1000000
    return val
       
def nstos(x):
    val = x/1000000000
    return val

def convert(x,y):
    if y == 'ms':
        return mstos(x)
    elif y == 'µs':
        return ustos(x)
    elif y == 'ns':
        return nstos(x)
    else:
        return x
    
    