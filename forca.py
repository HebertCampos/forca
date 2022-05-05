# Jogo da forca

import random

desenho = [
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
        else: 
            erros.append[letra]
        #print(f'letras erradas:\n{erros}')
        #print(f'letras certas:\n{acertos}')
    
    def perdeu(self):
        if len(desenho) > len(self.letra):
            return 0
        else: return 1
    
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
    
    while True:
        letra = input('digite letra: ')
        jogo.acertarLetra(letra)
        if jogo.perdeu() == 0:
            break
        

if __name__ == "__main__":
    main()