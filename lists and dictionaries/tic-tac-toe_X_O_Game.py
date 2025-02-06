X_O_matrix = {'1':'1','2':'2','3':'3',
          '4':'4','5':'5','6':'6',
          '7':'7','8':'8','9':'9'}
def printX_O_matrix(X_O_matrix):
    print(X_O_matrix['1'] + '|' + X_O_matrix['2'] + '|' + X_O_matrix['3'])
    print(X_O_matrix['4'] + '|' + X_O_matrix['5'] + '|' + X_O_matrix['6'])
    print(X_O_matrix['7'] + '|' + X_O_matrix['8'] + '|' + X_O_matrix['9'])

def main():
    player_x= 'x'
    player_o= 'o'
    select_player = player_x.lower()
    count = 1
    printX_O_matrix(X_O_matrix)
    while count <= 9:
        choose_index = input(f'Player {select_player}, please choose the index (1-9): ')
        if choose_index not in X_O_matrix:
            print('Invalid index. Please choose a number between 1 and 9.')

        if X_O_matrix[choose_index] not in ['x', 'o']:
            X_O_matrix[choose_index] = select_player
            print(count)
            printX_O_matrix(X_O_matrix)
        else:
            print('this index filled please choose other index')
            print(count)
            continue

        if count >= 5:
            if X_O_matrix['1'] == X_O_matrix ['2'] == X_O_matrix ['3']:
                print(f'*' *5, 'Game Over', '*' *15)
                print(f'*' *5, f'the player {select_player} is win', '*' *5)
                print(f'*' *5, 'Game Over', '*' *15)
                break
            elif X_O_matrix['4'] == X_O_matrix ['5'] == X_O_matrix ['6']:
                print(f'*' * 5, 'Game Over', '*' * 15)
                print(f'*' * 5, f'the player {select_player} is win', '*' * 5)
                print(f'*' * 5, 'Game Over', '*' * 15)
                break
            elif X_O_matrix['7'] == X_O_matrix ['8'] == X_O_matrix ['9']:
                print(f'*' * 5, 'Game Over', '*' * 15)
                print(f'*' * 5, f'the player {select_player} is win', '*' * 5)
                print(f'*' * 5, 'Game Over', '*' * 15)
                break
            elif X_O_matrix['1'] == X_O_matrix ['4'] == X_O_matrix ['7']:
                print(f'*' * 5, 'Game Over', '*' * 15)
                print(f'*' * 5, f'the player {select_player} is win', '*' * 5)
                print(f'*' * 5, 'Game Over', '*' * 15)
                break
            elif X_O_matrix['2'] == X_O_matrix ['5'] == X_O_matrix ['8']:
                print(f'*' * 5, 'Game Over', '*' * 15)
                print(f'*' * 5, f'the player {select_player} is win', '*' * 5)
                print(f'*' * 5, 'Game Over', '*' * 15)
                break
            elif X_O_matrix['3'] == X_O_matrix ['6'] == X_O_matrix ['9']:
                print(f'*' * 5, 'Game Over', '*' * 15)
                print(f'*' * 5, f'the player {select_player} is win', '*' * 5)
                print(f'*' * 5, 'Game Over', '*' * 15)
                break
            elif X_O_matrix['1'] == X_O_matrix ['5'] == X_O_matrix ['9']:
                print(f'*' * 5, 'Game Over', '*' * 15)
                print(f'*' * 5, f'the player {select_player} is win', '*' * 5)
                print(f'*' * 5, 'Game Over', '*' * 15)
                break
            elif X_O_matrix['3'] == X_O_matrix ['5'] == X_O_matrix ['7']:
                print(f'*' * 5, 'Game Over', '*' * 15)
                print(f'*' * 5, f'the player {select_player} is win', '*' * 5)
                print(f'*' * 5, 'Game Over', '*' * 15)
                break

            if count == 9:
                print(f'*' * 5, 'Game Over', '*' * 15)
                print(f'*' * 5, 'The result is a draw.', '*' * 5)
                print(f'*' * 5, 'Game Over', '*' * 15)
                break

        count +=1
        select_player = player_o if select_player == player_x.lower() else player_x.lower()

if __name__ == "__main__":
    main()