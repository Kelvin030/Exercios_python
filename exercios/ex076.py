produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
print('='*50)
print(f'{"lista de preços":^50}')
print('='*50)
for item in range(0, len(produtos), 2):
    print(f'{produtos[item]:.<40}',f'R$ {float(produtos[item+1]):<40}')
print('='*50)
