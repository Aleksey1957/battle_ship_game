from random import *


class Field:
    def __init__(self, size, ships):
        self.size = size
        self.ships_alive = ships
        self.grid = []
        for _ in range(size):
            self.grid.append([None] * size)

    def display(self, show_ships=True):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        new_letters = '    '
        for letter in letters:
            new_letters += letter
            new_letters += ' '
        print(new_letters)

        for i, row in enumerate(self.grid):
            display_row = ""
            for cell in row:

                if cell is None or (cell is not None and not show_ships):
                    display_row += "O "
                else:
                    display_row += "■ "
            if i + 1 != 10:  # вывод ноликов и квадратиков
                print(i + 1, " ", display_row)
            else:
                print(i + 1, "", display_row)


class BattleshipGame:
    def __init__(self):
        self.size = 10
        self.ships = 15
        self.player_field = Field(self.size, self.ships)
        self.computer_field = Field(self.size, self.ships)

    # Это функция расстановки кораблей, она уже полностью написана
    def place_ships_randomly(self, field, ships):
        for _ in range(ships):
            placed = False
            while not placed:
                coords = (randint(0, self.size - 1), randint(0, self.size - 1))
                if self.is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = "S"
                    placed = True

    # Это функция проверки расстановки кораблей, она уже полностью написана
    def is_valid_ship_placement(self, field, coords, ship_length=1, ):
        x, y = coords

        # Проверка на наличие соседних клеток по горизонтали и вертикали
        for i in range(ship_length + 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    new_x, new_y = x + j, y + k
                    if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == "S":
                        return False

        return True

    def player_turn(self, x, y):
        x = 'ABCDEFGHIJ'.index(x)
        y -= 1
        if self.computer_field.grid[y][x] == 'S':
            self.computer_field.grid[y][x] = 'X'
            print("Вы попали!")
            self.computer_field.ships_alive -= 1
        else:
            print("Промах!")

    def computer_turn(self):
        x = randint(0, self.size - 1)
        y = randint(0, self.size - 1)
        if self.player_field.grid[y][x] == 'S':
            self.player_field.grid[y][x] = 'X'
            print("Компьютер попал!")
            self.player_field.ships_alive -= 1
        else:
            print("Компьютер промахнулся!")

    def play(self):
        print("Расстановка кораблей компьютера:")
        self.place_ships_randomly(self.computer_field, self.ships)
        self.computer_field.display()

        print("Ваша расстановка кораблей:")
        self.place_ships_randomly(self.player_field, self.ships)
        self.player_field.display(True)

        while True:
            print('Ваш ход: ')
            x = input('Введите координату по X: ').upper()
            y = int(input('Введите координату по Y: '))
            self.player_turn(x, y)
            if self.computer_field.ships_alive == 0:
                print("Вы победили! Все корабли компьютера потоплены.")
                break
            print('Ход компьютера: ')
            self.computer_turn()
            if self.player_field.ships_alive == 0:
                print("Вы проиграли! Все ваши корабли потоплены.")
                break


game = BattleshipGame()
game.play()
