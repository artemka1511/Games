list = ['-', '-', '-', '-', '-', '-', '-', '-', '-']


def game_turn(game_token):
    valid = False
    while not valid:
        try:
            turn = int(input('Введите координатную цифру для ' + game_token + ' (подсказка справа): '))
            if 1 <= turn <= 9:
                if list[turn-1] not in 'X0':
                    list[turn-1] = game_token
                    valid = True
                else:
                    print('')
                    print('ERROR ERROR ERROR: Данная клетка уже занята. Введите другое значение')
            else:
                print('')
                print('ERROR ERROR ERROR: Введено неправильное значение ( введите значение от 1 до 9 )')
        except ValueError:
            print('')
            print('ERROR ERROR ERROR: Необходимо ввести цифровое значение')


def game():
    i = 0
    while i <= 9:
        if list[0] == list[1] == list[2] == 'X' or list[0] and list[1] == list[2] == '0'\
                or list[3] == list[4] == list[5] == 'X' or list[3] == list[4] == list[5] == '0' \
                or list[6] == list[7] == list[8] == 'X' or list[6] == list[7] == list[8] == '0' \
                or list[0] == list[3] == list[6] == 'X' or list[0] == list[3] == list[6] == '0' \
                or list[1] == list[4] == list[7] == 'X' or list[1] == list[4] == list[7] == '0' \
                or list[2] == list[5] == list[8] == 'X' or list[2] == list[5] == list[8] == '0' \
                or list[0] == list[4] == list[8] == 'X' or list[0] == list[4] == list[8] == '0' \
                or list[2] == list[4] == list[6] == 'X' or list[2] == list[4] == list[6] == '0':
            print('Игра окончена: ПОБЕДА')
            break
        else:
            print(' |  {}  |  {}  |  {}  |           |  1  |  2  |  3  |\n'.format(list[0], list[1], list[2]),
                  '|  {}  |  {}  |  {}  |           |  4  |  5  |  6  |\n'.format(list[3], list[4], list[5]),
                  '|  {}  |  {}  |  {}  |           |  7  |  8  |  9  |\n'.format(list[6], list[7], list[8]))
            if i == 0 or i == 2 or i == 4 or i == 6 or i == 8:
                game_turn('X')
            else:
                game_turn('0')
            i += 1
            if i == 9:
                print('')
                print('Игра окончена: НИЧЬЯ')
                break


game()


