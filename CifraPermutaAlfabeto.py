from CifraDeCesar import CifraDeCesar

class CifraPermutaAlfabeto(CifraDeCesar):
    def __init__(self, alfabeto = 'abcdefghijklmnopqrstuvwxyz'):
        super().__init__(alfabeto)

    def codifica(self, texto: str, chave: str):
        texto = self.prepara_texto_bruto(texto)
        if len(chave) != self._tamanho_alfabeto:
            raise ValueError('Comprimento da chave invalido.')
                            
        abc_encode = dict(zip(
            self._alfabeto,
            chave
        ))
        cifra = [abc_encode.get(t, t) for t in texto]
        return ''.join(cifra)
    
    def decodifica(self, cifra: str, chave: str):
        if len(chave) != self._tamanho_alfabeto:
            raise ValueError('Comprimento da chave invalido.')
        
        abc_decode = dict(zip(
            chave,
            self._alfabeto
        ))
        txt_plano = [abc_decode.get(c, c) for c in cifra]
        return ''.join(txt_plano)
