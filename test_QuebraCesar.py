import pytest
from QuebraCesar import QuebraCesar
from Util import le_arquivo

@pytest.fixture
def qc():
    return QuebraCesar()

def test_peso_do_simbolo(qc):
    assert qc.peso_do_simbolo('a') == 1
    assert qc.peso_do_simbolo('e') == 1
    assert qc.peso_do_simbolo('i') == 1
    assert qc.peso_do_simbolo('o') == 1
    assert qc.peso_do_simbolo('u') == 1
    
    assert qc.peso_do_simbolo('b') == -1
    assert qc.peso_do_simbolo('z') == -1
    
    assert qc.peso_do_simbolo(' ') == 0
    assert qc.peso_do_simbolo('ã') == 0
    assert qc.peso_do_simbolo('ç') == 0
    assert qc.peso_do_simbolo('é') == 0

def test_soma_pesos(qc):
    assert qc.soma_pesos('a e i o u') == 5
    assert qc.soma_pesos('x y z') == -3
    assert qc.soma_pesos('éç ã!') == 0
    assert qc.soma_pesos('pão') == 0
    assert qc.soma_pesos('abacate') == 1
    assert qc.soma_pesos('verde') == -1
    assert qc.soma_pesos('trator') == -2
    assert qc.soma_pesos('arrozcomfeijão') == -1

def test_ataque_bruto_str_curta(qc):
    resultado =  qc.ataque_bruto('riifqtfdwvzaãf')
    assert resultado[0]["peso"] == -1
    assert resultado[0]["chave_gerada"] == 17
    assert resultado[0]["texto_plano"] == "arrozcomfeijão"

    resultado = qc.ataque_bruto('Jaaxi Lxv Onrsãx')
    assert resultado[0]["peso"] == -1
    assert resultado[0]["chave_gerada"] == 9
    assert resultado[0]["texto_plano"] == "arrozcomfeijão"

    resultado = qc.ataque_bruto('Duurc Frp Ihlmãr')
    assert resultado[0]["peso"] == -1
    assert resultado[0]["chave_gerada"] == 3
    assert resultado[0]["texto_plano"] == "arrozcomfeijão"

def test_ataque_bruto_txt_longo(qc):
    chave, txt_cifra = le_arquivo('txt_cifrado_cesar.txt')
    _,txt_plano = le_arquivo('texto_plano.txt')
    
    resultado =  qc.ataque_bruto(txt_cifra)
    assert resultado[0]['chave_gerada'] == int(chave)
    assert resultado[0]['texto_plano'] == qc._c.prepara_texto_bruto(txt_plano)
    