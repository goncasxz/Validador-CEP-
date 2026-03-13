import pytest
from validador import validar_cep

def test_validador_cep_sorocaba_valido():
    assert validar_cep("18.050-100", "Sorocaba") == True
git
def test_validador_cep_votorantim_invalido():
    assert validar_cep("19.000-000", "Votorantim") == False

def test_validador_cep_votorantim_valido():
    assert validar_cep("18110-000", "Votorantim") == True

def test_validador_cep_apenas_numeros():
    assert validar_cep("18110000", "Votorantim") == True