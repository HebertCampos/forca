# Jogo da forca

import random

forca = [
    '''
    -------
    |     |
    |     
    |    
    |    
    |            
=================
    '''
,
    '''
    -------
    |     |
    |     O
    |    
    |    
    |            
=================
    ''',
    '''
    -------
    |     |
    |     O
    |     |
    |    
    |           
=================
    ''',
    '''
    -------
    |     |
    |     O
    |    /|
    |    
    |           
=================
    ''',
    '''
    -------
    |     |
    |     O
    |    /|\
    |    
    |            
=================
    ''',
    '''
    -------
    |     |
    |     O
    |    /|\
    |    / 
    |            
=================
    ''',
    '''
    -------
    |     |
    |     O
    |    /|\
    |    / \
    |           
=================
    '''
]

class Forca:
    def __init__(self, palavra):
        self.palavra = palavra
    
    def acertarLetra(self, letra):
        self.letra = letra
    
    def perdeu(self):
        pass
    
    def ganhou(self):
        pass
    
    def mostrar_letra(self):
        pass
    
    def status(self):
        pass
    
def pegando_palavra():
    with open('palavras.txt', 'rt') as f:
        banco = f.readlines()
    return banco[random.randint(0, len(banco))].strip()

def main():
    jogo = Forca(pegando_palavra())