from CifraDeCesar import CifraDeCesar
from pprint import pprint
import string


class QuebraCesar:
    def __init__(self, cifra: str = '', alfabeto: str = string.ascii_lowercase):
        self._alfabeto: str = alfabeto
        self._cifra: str = cifra
        self._c = CifraDeCesar()
        self._tentativas = []

    # Setter
    def set_cifra(self, texto_cifrado: str) -> None:
        if not isinstance(texto_cifrado, str):
            raise ValueError("O alfabeto deve ser uma string.")
        if len(texto_cifrado) == 0:
            raise ValueError("O alfabeto não pode ser vazio.")
        self._cifra = texto_cifrado
        self._tentativas = []

    def peso_do_simbolo(self, simbolo) -> int:
        if not simbolo in self._alfabeto: 
            return 0
        if simbolo in 'aeiou':
            return 1
        return -1
    
    def soma_pesos(self, texto) -> int:
        self._distancia_do_zero = sum(map(self.peso_do_simbolo, texto))
        return self._distancia_do_zero

    def ataque_bruto(self, cifra: str) -> list:
        self.set_cifra(cifra)
        for chave_gerada in range(1, len(self._c._alfabeto)):
            texto_plano = self._c.decodifica(self._cifra, chave_gerada)
            peso = self.soma_pesos(texto_plano)
            self._tentativas.append({
                'chave_gerada': chave_gerada,
                'texto_plano': texto_plano,
                'peso': peso
            })
        return self.ranking_peso_crescente()
    
    def ranking_peso_crescente(self)-> dict:
        ordenado = sorted(self._tentativas, key=lambda item: abs(float(item['peso'])))
        return ordenado
