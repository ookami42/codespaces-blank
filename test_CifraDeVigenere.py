import pytest
from CifraDeVigenere import CifraDeVigerere
from Util import le_arquivo

@pytest.fixture
def vigenere():
    return CifraDeVigerere()

def test_set_chave_encode(vigenere):
    chave = 'zabc'
    vigenere.set_chave_encode(chave)
    assert vigenere.get_next_chave() == 25 # z
    assert vigenere.get_next_chave() == 0  # a
    assert vigenere.get_next_chave() == 1  # b
    assert vigenere.get_next_chave() == 2  # c
    assert vigenere.get_next_chave() == 25 # z
    assert vigenere.get_next_chave() == 0  # a

def test_set_chave_decode(vigenere):
    chave = 'abcz'
    vigenere.set_chave_decode(chave)
    assert vigenere.get_next_chave() == 0  # -a
    assert vigenere.get_next_chave() == 25 # -b
    assert vigenere.get_next_chave() == 24 # -c
    assert vigenere.get_next_chave() == 1  # -z
    assert vigenere.get_next_chave() == 0  # -a
    assert vigenere.get_next_chave() == 25 # -b

def test_codifica_str(vigenere):
    assert vigenere.codifica('Arroz e Feijão', 'abc') == 'astoagffkjãp'
    assert vigenere.codifica('Arroz e Feijão', 'mensagemsecreta') == vigenere.prepara_texto_bruto('Mvegz k Jqanãq')

def test_codifica_txt(vigenere):
    _, txt_plano = le_arquivo('texto_plano.txt')
    chave, txt_cifrado = le_arquivo('txt_cifrado_vigenere.txt')
    assert vigenere.codifica(txt_plano, chave) == vigenere.prepara_texto_bruto(txt_cifrado)

def test_decodifica_str(vigenere):
    assert vigenere.decodifica('astoagffkjãp', 'abc') == 'arrozefeijão'
    assert vigenere.decodifica('Mvegz k Jqanãq', 'mensagemsecreta') == 'arrozefeijão'
    
def test_decodifica_txt(vigenere):
    _, txt_plano = le_arquivo('texto_plano.txt')
    chave, txt_cifrado = le_arquivo('txt_cifrado_vigenere.txt')
    assert vigenere.decodifica(txt_cifrado, chave) == vigenere.prepara_texto_bruto(txt_plano)

def test_eh_reversivel(vigenere):
    msg_original = 'umafrasedeexemploemtextoplano'
    chave = 'chavevigenere'
    msg_cifrada = 'wtaavvakhrioiowljihbkbgsgpcuo'

    resultado1 = vigenere.codifica(msg_original, chave)
    resultado1 = vigenere.decodifica(resultado1, chave)
    assert resultado1 == msg_original

    resultado2 = vigenere.decodifica(msg_cifrada, chave)
    resultado2 = vigenere.codifica(resultado2, chave)
    assert resultado2 == msg_cifrada
