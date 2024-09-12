# Função que retorna ture se o número for positivo ou seja > 0

def is_positive(numero):
    return numero > 0


def test_eh_positivo():
    assert is_positive(5) is True
    assert is_positive(-5) is False

# exemplo de teste quebrando pois queremos garantir que retorne um False,
# porem 2 é um numero positivo, retornando True
# assert is_positive(2) is False
