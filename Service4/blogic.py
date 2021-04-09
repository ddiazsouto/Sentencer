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


class BeLogic():
    def __init__(self, phrase, sentence):
        self.phrase = phrase
        self.sentence = sentence


    def color(self):
        
        def tones(mood):
        
            if mood == 1 or mood == 0:
                happy = ["XYXY00", "XY5500", "XY00XY", "XY0000"]
                return happy[azar([0, 3], 1)]
            else:
                sad = ["0000XY", "00XY00", "00XYXY", "0XYXY0", "XYXYXY"]
                return sad[azar([0, 4], 1)]
            
        def depth(boolean):        
            hexa = '0123456789abcdef'
            
            if boolean == False:
                pair = azar([0, 7], 2)
                return hexa[pair[0]] + hexa[pair[1]]
            else:
                pair = azar([8, 15], 2)
                return hexa[pair[0]] + hexa[pair[1]]
        
        
        color = tones(self.sentence["mood"])           
        darkness = depth(self.phrase["dark"])
        
        color = color.replace('XY', darkness)
                    
        return color

    
    def talk(self):
                
        def togetherness(jason, exp):
            
            outcome = ''
            
            if jason['question'] == True:
                
                state = jason['phrase']                
                outcome = state['aux'] +' '+ state['pronoun'] +' '+ state['verb1'] +' '+ state['verb2'] + '? '+ exp
                
            else:
                ask = jason['phrase']
                outcome = exp + '. '+ ask['pronoun'] +' ' + ask['verb1'] +' ' + ask['verb2'] 
                
            return outcome
                              
        
        expression = self.sentence['expression']        
        myson = self.phrase
        
        return togetherness(myson, expression)




