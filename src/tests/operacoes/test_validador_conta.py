import pytest
from src.tech.claramaracaja.operacoes.validador_conta import validar_abertura_conta


def test_aprova_conta_com_idade_e_score_validos():
	assert validar_abertura_conta(20, 800) == "Aprovado"


def test_recusa_conta_com_score_igual_a_200():
	assert validar_abertura_conta(20, 200) == "Recusado"


def test_recusa_conta_com_score_abaixo_de_500():
	assert validar_abertura_conta(20, 499) == "Recusado"


def test_impede_abertura_para_menor_de_idade():
	with pytest.raises(ValueError, match="Menor de idade não permitido"):
		validar_abertura_conta(17, 800)

