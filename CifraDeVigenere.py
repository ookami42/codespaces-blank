from CifraDeCesar import CifraDeCesar
from itertools import cycle

class CifraDeVigerere(CifraDeCesar):
    def __init__(self, alfabeto = 'abcdefghijklmnopqrstuvwxyz'):
        super().__init__(alfabeto)
        self._tabela_deslocamento = {a: i for i, a in enumerate(self._alfabeto)}

    def set_chave_encode(self, chave: str) -> None:
        invalidos = [c for c in chave if c not in self._alfabeto]

        if invalidos:
            raise ValueError(f"Caracteres inválidos: {invalidos}")

        self.chave_circular = cycle(
            [self._tabela_deslocamento.get(c) for c in chave]
        )

    def get_next_chave(self) -> int:
        return next(self.chave_circular)
    
    def aplica_chave(self, texto) -> str:
        texto_plano = self.prepara_texto_bruto(texto)        
        cifra = []
        for t in texto_plano:
            if t in self._alfabeto:
                c = self.get_next_chave()
                cifra.append(self.desloca(t, c))
            else:
                cifra.append(t)

        return ''.join(cifra)
    
    def set_chave_decode(self, chave: str) -> None:
        invalidos = [c for c in chave if c not in self._alfabeto]

        if invalidos:
            raise ValueError(f"Caracteres inválidos: {invalidos}")

        self.chave_circular = cycle(
            [-(self._tabela_deslocamento.get(c)) % self._tamanho_alfabeto 
                for c in chave]
        )

    def codifica(self, texto: str, chave: str) -> str:
        self.set_chave_encode(chave)
        cifra = self.aplica_chave(texto)
        return cifra

    def decodifica(self, texto, chave) -> str:
        self.set_chave_decode(chave)
        texto_plano = self.aplica_chave(texto)
        return texto_plano
            

CifraDeVigerere().codifica('Arroz e Feijão', 'mensagemsecreta')
CifraDeVigerere().decodifica('Mvegz k Jqanãq', 'mensagemsecreta')