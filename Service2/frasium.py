from random import randint


def azar(rang, numbers):

    buffer = []
    lowl  = rang[0]
    highl = rang[1]

    for i in range(numbers):
        buffer.append(randint(lowl, highl))
        
    if len(buffer)==1:
        buffer=buffer[0]

    return buffer


def binary():
    random = azar([1, 1000], 1)
    
    if random%2==0:
        return False
    else:
        return True