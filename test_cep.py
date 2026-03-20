import pytest
from validador import validar_cep

def test_validador_cep_sorocaba_valido():
    assert validar_cep("18.050-100", "Sorocaba") == True

def test_validador_cep_votorantim_invalido():
    assert validar_cep("19.000-000", "Votorantim") == False

def test_validador_cep_votorantim_valido():
    assert validar_cep("18110-000", "Votorantim") == True

def test_validador_cep_capela_do_alto_valido():
    assert validar_cep("18195-100", "Capela do Alto") == True

def test_validador_cep_sao_roque_valido():
    assert validar_cep("18130-150", "Sao Roque") == True

def test_validador_cep_itu_valido():
    assert validar_cep("13301-201", "Itu") == True

def test_validador_cep_campinas_valido():
    assert validar_cep("13015-100", "Campinas") == True

def test_validador_cep_boituva_valido():
    assert validar_cep("18555-000", "Boituva") == True

def test_validador_cep_jundiai_valido():
    assert validar_cep("13200-500", "Jundiai") == True

def test_validador_cep_piracicaba_valido():
    assert validar_cep("13400-100", "Piracicaba") == True

def test_validador_cep_limeira_valido():
    assert validar_cep("13480-100", "Limeira") == True

def test_validador_cep_americana_valido():
    assert validar_cep("13465-100", "Americana") == True

def test_validador_cep_apenas_numeros():
    assert validar_cep("18110000", "Votorantim") == True

def test_validador_cidade_fantasma():
    assert validar_cep("18050-100", "Gotham City") == False

def test_validador_erro_digitacao_letras():
    assert validar_cep("18A050-10", "Sorocaba") == False

def test_validador_cep_incompleto():
    assert validar_cep("18050", "Sorocaba") == False

def test_validador_cep_longo():
    assert validar_cep("18050-100999", "Sorocaba") == False