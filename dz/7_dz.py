# Создайте программу, которая реализует игру «Крестики-нолики».
# Для этого напишите:
# 1. Класс, который будет описывать поле игры.
# class Board:
# # Класс поля, который создаёт у себя экземпляры клетки.
# # Пусть класс хранит информацию о состоянии поля (это может быть список из
# девяти элементов).
# # Помимо этого, класс должен содержать методы:
# # «Изменить состояние клетки». Метод получает номер клетки и, если клетка не
# занята, меняет её состояние. Если состояние удалось изменить, метод возвращает
# True, иначе возвращается False.
# # «Проверить окончание игры». Метод не получает входящих данных, но
# возвращает True/False. True — если один из игроков победил, False — если
# победителя нет.
# 2. Класс, который будет описывать одну клетку поля:
# class Cell:
# # Клетка, у которой есть значения:
# # занята она или нет;
# # номер клетки;
# # символ, который клетка хранит (пустая, крестик, нолик).
# 3. Класс, который описывает поведение игрока:
# class Player:
# # У игрока может быть:
# # имя,
# # количество побед.
# # Класс должен содержать метод:
# # «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер
# клетки). Введённый номер нужно обязательно проверить.
# 4. Класс, который управляет ходом игры:
# class Game:
# # класс «Игры» содержит атрибуты:
# # состояние игры,
# # игроки,
# # поле.
# # А также методы:
# # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у
# игрока номер клетки, изменяет поле, проверяет, выиграл ли игрок. Если игрок победил,
# возвращает True, иначе False.
# # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который
# завершается победой одного из игроков или ничьей. Если игра завершена, метод
# возвращает True, иначе False.
# # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой
# игры, хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт
# игроков.

class Cell:
    def __init__(self, cell_number):
        self.cell_number = cell_number
        self.symbol = None

    def set_symbol(self, symbol):
        if self.symbol is None:
            self.symbol = symbol
            return True
        return False


class Board:
    def __init__(self, cells=None):
        if cells is None:
            cells = [Cell(i) for i in range(9)]
        self.cells = cells

    def change_cell_state(self, cell_number, symbol):
        return self.cells[cell_number].set_symbol(symbol)

    def check_winner(self):
        winner_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combination in winner_combinations:
            if (self.cells[combination[0]].symbol == self.cells[combination[1]].symbol ==
                self.cells[combination[2]].symbol and
                self.cells[combination[0]].symbol is not None):
                return True
        return False

    def reset(self):
        for cell in self.cells:
            cell.symbol = None


class Player:
    def __init__(self, name):
        self.name = name
        self.count_of_wins = 0

    def make_move(self):
        while True:
            move = int(input('Выбери клетку, которой будешь ходить (0 - 8): '))
            if 0 <= move <= 8:
                return move
            else:
                print("Некорректный ввод. Попробуйте снова.")


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Игрок 1"), Player("Игрок 2")]
        self.current_player_index = 0

    def start_turn(self):
        current_player = self.players[self.current_player_index]
        move = current_player.make_move()
        if self.board.change_cell_state(move, 'X' if self.current_player_index == 0 else 'O'):
            if self.board.check_winner():
                print(f'Поздравляем! {current_player.name} выиграл!')
                current_player.count_of_wins += 1
                return True
            self.current_player_index = (self.current_player_index + 1) % 2
        else:
            print("Эта клетка уже занята. Попробуйте другую.")
        return False

    def start_game(self):
        while True:
            self.board.reset()
            game_over = False

            while not game_over:
                game_over = self.start_turn()
                if game_over:
                    break
                if all(cell.symbol is not None for cell in self.board.cells):
                    print("Ничья!")
                    break

            print(f"Текущий счет: {self.players[0].name}: {self.players[0].count_of_wins}, {self.players[1].name}: {self.players[1].count_of_wins}")

            again = input("Хотите сыграть еще раз? (да/нет): ").lower()
            if again != 'да':
                break


if __name__ == "__main__":
    game = Game()
    game.start_game()
