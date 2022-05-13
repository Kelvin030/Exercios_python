def leiaInt(msg='Digite um numero Inteiro'):
    while True:
        try:
            num = int(input(f'{msg}: '))
        except Exception as erro:
            print(f'\033[1;31m{erro.__class__}!!! Digite um numero Real valido valido\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mO usuario interrompeu o programa\033[m')
            break
            return 0
        else:
            break
    return num


def leiaFloat(msg='Digite um numero Real'):
    while True:
        try:
            num = float(input(f'{msg}: '))
        except Exception as erro:
            print(f'\033[1;31m{erro.__class__}!!! Digite um numero Real valido valido\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mO usuario interrompeu o programa\033[m')
            break
            return 0
        else:
            break
    return num
