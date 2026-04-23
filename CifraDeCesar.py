class CifraDeCesar:
    def __init__(self, alfabeto: str = 'abcdefghijklmnopqrstuvwxyz'):
        self._alfabeto = alfabeto
        self._tamanho_alfabeto = 26

    # Getter
    def get_alfabeto(self) -> str:
        return self._alfabeto

    # Setter
    def set_alfabeto(self, novo_alfabeto: str)-> None:
        if not isinstance(novo_alfabeto, str):
            raise ValueError('O alfabeto deve ser uma string.')
        if len(novo_alfabeto) == 0:
            raise ValueError('O alfabeto não pode ser vazio.')
        self.tamanho_alfabeto = len(novo_alfabeto)
        self._alfabeto = novo_alfabeto

    def prepara_texto_bruto(self, texto_bruto: str) -> str:
        texto_limpo = texto_bruto.lower().replace(' ', '')
        return texto_limpo

    def desloca(self, letra: str, deslocamento: int=3) -> str:
        if letra not in self._alfabeto: 
            return letra
        indice_cifrado = (self._alfabeto.index(letra) + deslocamento) % self._tamanho_alfabeto
        return self._alfabeto[indice_cifrado]
    
    def codifica(self, texto: str, chave: int) -> str:
        texto = self.prepara_texto_bruto(texto)
        cifra = ''.join(self.desloca(simbolo, chave) for simbolo in texto)
        return cifra
    
    def decodifica(self, cifra: str, chave: int) -> str:
        chave_complementar = (-chave) % self._tamanho_alfabeto
        texto_plano = self.codifica(cifra, chave_complementar)
        return texto_plano
