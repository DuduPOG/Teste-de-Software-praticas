print("Digite 3 lados de um triângulo para verficar qual é seu tipo:")
print("Tipos possíveis:")
print("Equilátero, todos os lados iguais")
print("Isósceles, dois lados iguais")
print("Escaleno, nenhum lado igual")

lado_a = int(input("Lado A: "))

lado_b = int(input("Lado B: "))

lado_c = int(input("Lado C: "))

# Função que retorna qual é o tipo de triângulo com base na entrada de seus três lados
def qualTrianguloEh(a: int, b: int, c: int) -> str:
    
    if (lado_a == lado_b and lado_b == lado_c):
        return "Equilátero"
    elif (lado_a == lado_b or lado_a == lado_c or lado_b == lado_c):
        return "Isósceles"
    else:
        return "Escaleno"
    
"""
def ehValido(a: int, b: int, c: int):
"""
    

print(qualTrianguloEh(lado_a, lado_b, lado_c))
    
