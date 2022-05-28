import functions
import menu


menu = menu.menu()
menu.main_menu('PokeDex')
menu.options('Pesquisar por Nome ou ID', 'Lista de IDs', 'Sair')
choice = int(input("Sua Opção: "))

if choice == 1:
    functions.search()