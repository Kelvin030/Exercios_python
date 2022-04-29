lista = ("Palmeiras", "Flamengo", "Internacional", "Grêmio", "São Paulo", "Atlético-MG",
         "Athletico-PR","Cruzeiro","Botafogo""Santos","Bahia", "Fluminense", "Corinthians",
         "Chapecoense", "Ceara""Vasco", "Sport", "América-MG", "Vitória", "Paraná")
print("=-"*40)
print('lista dos times do brasileirão:', lista)
print("=-"*40)
print(f"os 5 primeiros times do brasileirão são:{lista[:5]}")
print("=-"*40)
print(f"os 4 últimos times do brasileirão são: {lista[-4:]}")
print("=-"*40)
print(f'os times do brasileirão em ordem alfabetica: {sorted(lista)}')
print("=-"*40)
print(f'o time da Chapecoense esta na posição: {lista.index("Chapecoense")+1}')
