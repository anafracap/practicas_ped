def crear_multiplicador(n):
    def multiplicador_interior(x):
        return x * n
    return multiplicador_interior

# multiplicador de 3
por3 = crear_multiplicador(3)

# multiplicador de 5
por5 = crear_multiplicador(5)

# Output: 27
print(por3(9))

# Output: 15
print(por5(3))

# Output: 30
print(por5(por3(2)))
