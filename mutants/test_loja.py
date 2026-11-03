from loja import calcular_desconto

def test_compra_acima_de_100_sem_fidelidade():
    # 200 - 10% = 180
    assert calcular_desconto(200.0, fidelidade=False) == 180.0
def test_compra_abaixo_de_100_com_fidelidade():
    # 50 - 5% = 47.5
    assert calcular_desconto(50.0, fidelidade=True) == 47.5