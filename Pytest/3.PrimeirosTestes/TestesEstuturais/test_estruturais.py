
def test_listas_iguais():
    lista_esperada = [1,2,3,4,5]
    lista_resultado = [1,2,3,4,5]
    # Pode ser colocado uma mensagem no assert caso o resultado falhe,
    # serve para analises
    assert lista_resultado == lista_esperada, "As listas não são iguais."