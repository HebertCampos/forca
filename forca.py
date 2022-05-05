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
        acertos = []
        erros = []
        self.letra = letra
        if letra in self.palavra:
            acertos.append[letra]
        else: erros.append[letra]
        print(f'letras erradas:\n{[l for l in erros]}')
        print(f'letras certas:\n{[l for l in acertos]}')
    
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