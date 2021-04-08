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

    positive = ['It was the gratest thing that my eyes have yet seen!!', 'How great', 'Absolutely tremendous!!', 'Holly Cow!!', \
    'Awesome', 'Just like a fish in the water', 'Makes me so happy!', 'Yeeah baby!!', 'Not bad at all', 'Fantastic!', 'Nice!']

    negative = ['Just horrible', 'Do not even try man...', 'Could be better', 'Holly Cow!!', \
    'Horrendous!!', 'Please, that is enough', 'Who cares?', 'Bad, bad, bad...', 'I better leave now.', 'That is just so baaaad!', 'Can not stand it anymore']

    output = dict()

    if 1 == 1:
        output['mood'] = 1
        output['expression'] = positive[azar([0, 10], 1)]
    elif 1 == 0:
        output[0] = negative[azar([0, 10], 1)]         
    
    return output
