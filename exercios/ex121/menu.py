class menu():

    def main_menu(self, titulo):
        print('=' * 40 )
        print(f'{titulo}'.center(40))
        print('=' * 40 )


    def options(self,*options):
        cont = 1
        for item in options:
            print(f'{cont} - {item}')
            cont += 1
        print('=' * 40)

if __name__ == '__main__':
    menu = menu()
