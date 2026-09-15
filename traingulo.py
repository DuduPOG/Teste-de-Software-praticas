def qualTrianguloEh(a: int, b: int, c: int) -> str:
    lados = (a, b, c)

    if any(isinstance(lado, bool) or not isinstance(lado, (int, float)) for lado in lados):
        return "Entrada inválida"

    if any(lado <= 0 for lado in lados):
        return "Os lados devem ser positivos"

    maior_lado = max(lados)
    outros_lados = sum(lados) - maior_lado
    if outros_lados <= maior_lado:
        return "Os lados não formam um triângulo"

    if a == b == c:
        return "Equilátero"
    if a == b or a == c or b == c:
        return "Isósceles"
    return "Escaleno"

def ler_lado(nome: str):
    try:
        return float(input(f"Lado {nome}: "))
    except (TypeError, ValueError):
        return None

print("Digite 3 lados de um triângulo para verificar qual é seu tipo:")
print("Tipos possíveis: Equilátero, Isósceles e Escaleno")

lados = [ler_lado(nome) for nome in ("A", "B", "C")]
print(qualTrianguloEh(*lados))
