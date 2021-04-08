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


def expresser(mood):

    positive = ['It was the gratest thing that my eyes have yet seen!!', 'How great', 'Absolutely tremendous!!', 'Holly Cow!!', \
    'Awesome', 'Just like a fish in the water', 'Makes me so happy!', 'Yeeah baby!!', 'Not bad at all', 'Fantastic!', 'Nice!']

    negative = ['Just horrible', 'Do not even try man...', 'Could be better', 'Holly Cow!!', \
    'Horrendous!!', 'Please, that is enough', 'Who cares?', 'Bad, bad, bad...', 'I better leave now.', 'That is just so baaaad!', 'Can not stand it anymore']

    if mood == 1:
        return positive[azar([0, 10], 1)]
    elif mood ==0:
        return negative[azar([0, 10], 1)]         

