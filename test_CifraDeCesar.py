import pytest
from CifraDeCesar import CifraDeCesar

@pytest.fixture
def cesar():
    c = CifraDeCesar()
    abc_mais_espaco = c.get_alfabeto()
    c.set_alfabeto(abc_mais_espaco)
    return c

def test_prepara_texto_bruto(cesar):
    assert cesar.prepara_texto_bruto('Arroz Com Feijão') == 'arrozcomfeijão'

def test_desloca(cesar):
    assert cesar.desloca('a', 3) == 'd', 'a e chave 3 dá d'
    assert cesar.desloca('z', 2) == 'b', 'z e chave 2 dá b'
    assert cesar.desloca('x', 0) == 'x', 'x e chave 0 dá x'

def test_codifica(cesar):
    assert cesar.codifica('abc', 0) == 'abc'
    assert cesar.codifica('x y z', 0) == 'xyz'    
    assert cesar.codifica('a b c', 3) == 'def'
    assert cesar.codifica('xyz', 3) == 'abc'
    assert cesar.codifica('Arroz Com Feijão', 0) == 'arrozcomfeijão'
    assert cesar.codifica('Arroz Com Feijão', 17) == 'riifqtfdwvzaãf'
    assert cesar.codifica('Arroz Com Feijão', 9) == cesar.prepara_texto_bruto('Jaaxi Lxv Onrsãx')
    
def test_decodifica(cesar):
    assert cesar.decodifica('riifqtfdwvzaãf', 17) == 'arrozcomfeijão'
    assert cesar.decodifica('Jaaxi Lxv Onrsãx', 9) == 'arrozcomfeijão'
    assert cesar.decodifica('Duurc Frp Ihlmãr', 3) == 'arrozcomfeijão'
    assert cesar.decodifica('cdef', 3) == 'zabc'

def test_eh_reversivel(cesar):
    assert cesar.decodifica(cesar.codifica('palavra', 3), 3) == 'palavra'
    assert cesar.codifica(cesar.decodifica('palavra', 3), 3) == 'palavra'
