import random
from lib2to3.fixes.fix_metaclass import remove_trailing_newline
from symbol import return_stmt

player_name= input("please enter your name:")
print(f'hello {player_name}, you welcome in Simple guessing game')

list_of_Names = [
    "Ibrahim", "Ahmed", "Nawal", "Lubna", "Asia", "Aseel", "Raed", "Saed",
    "Abdulrahman", "Hanaa", "Khalid", "Fatima", "Zainab", "Yousef", "Salma",
    "Mariam", "Omar", "Hassan", "Layla", "Tariq"
]
print()
# print(list_of_Names)

random_name= random.choice(list_of_Names)
print(f'random name is:{random_name}')

try_nums= 1
suggested_name= input(f'you have 12 tries, please write your suggest name,(try number {try_nums}): ')
hint = ''
for i in range(12):
    # ''.join([char if char in suggest_name else '-' for char in random_name]) # chatgpt solution to fill hint var << here is better of my solution <<
    #      using for loop to fill hint var
        for char in random_name.lower():
            if char in suggested_name.lower():
                hint += char
            else:
                hint += '-'
        # print()
        if suggested_name.lower() == random_name.lower():
            print(f'your are win the name is "{random_name}"')
            break
        # else:
        else:
            print(f'Hint: Some letters of the name suggested by you ({hint}) are matching the letters of the correct name.',)
            hint =''
            try_nums +=1
        suggested_name = input(f'try again{try_nums}: ')

        print()
        if try_nums == 12:
            print('you are lose')
            break
