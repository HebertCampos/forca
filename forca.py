# Jogo da forca

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
        