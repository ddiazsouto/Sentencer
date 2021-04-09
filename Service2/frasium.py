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

def phraser(list, question):

    output = dict()

    pronoun = ['I', 'You', 'He', 'She', 'It',  'We', 'You', 'They']

    verb1 = ['like', 'adore', 'stay', 'get', 'prefer', 'belong', \
    'hate', 'despise']

    verb2 = ['jumping', 'watching', 'running', 'skipping', 'pointing', 'smelling', \
    'becoming', 'remaining']

    preposition = ['a', 'before', 'with', 'the', 'in', 'a', \
    'many', 'some']

    output['pronoun'] = pronoun[list[0]]
    output['verb1'] = verb1[list[1]]
    output['verb2'] = verb2[list[2]]
    output['preposition'] = preposition[list[3]]

    if question == True and output['pronoun'] in ['He', 'She', 'It']:
        output['aux'] = 'Does'
        output['pronoun'] = output['pronoun'].lower()
    elif question == True and output['pronoun'] not in ['He', 'She', 'It']:
        output['aux'] = 'Do'  
        if output['pronoun'] != 'I':
            output['pronoun'] = output['pronoun'].lower()
    
    return output  
