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

def phraser():

    pronoun = ['I', 'You', 'He', 'She', 'It',  'We', 'You', 'They']

    verb = ['jumping', 'watching', 'running', 'skipping', \
    'Horrendous!!', 'Please, that is enough', 'Who cares?', 'Bad, bad, bad...', 'I better leave now.', 'That is just so baaaad!', 'Can not stand it anymore']

    output = dict()

    if 1 == 1:
        output['mood'] = 1
        output['expression'] = positive[azar([0, 10], 1)]
    elif 1 == 0:
        output[0] = negative[azar([0, 10], 1)]         
    
    return output
