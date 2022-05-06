def area(lagura, comprimento):
    area = lagura * comprimento
    print(f"A área de {lagura} X {comprimento} é de {area}m²")


print("  Controle de Terrenos")
print("-" * 25)
lagura = float(input("Lagura (m): "))
comprimento = float(input("Comprimento (m): "))
area(lagura, comprimento)
