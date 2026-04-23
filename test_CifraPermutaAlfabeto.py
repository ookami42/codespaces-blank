from CifraPermutaAlfabeto import CifraPermutaAlfabeto
from Util import le_arquivo
import pytest

@pytest.fixture
def pa():
    return CifraPermutaAlfabeto()

_, txt = le_arquivo('texto_plano.txt')
chave, cifra = le_arquivo('txt_cifrado_permuta_alfabeto.txt')

def test_codifica(pa):
    cifra_esperada = pa.prepara_texto_bruto(cifra)
    resultado = pa.codifica(txt, chave)
    assert resultado == cifra_esperada

def test_decodifica(pa):
    txt_esperado = pa.prepara_texto_bruto(txt)
    resultado = pa.decodifica(cifra, chave)
    assert resultado == txt_esperado
