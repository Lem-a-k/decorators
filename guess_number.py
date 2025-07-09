from datetime import datetime as dt
from random import randint

from access_control import access_control
from constants import ADMIN_USERNAME, UNKNOWN_COMMAND


class GuessNumberGame:
    MIN_NUM = 1
    MAX_NUM = 100

    def __init__(self):
        self.username = None
        self.start_time = None
        self._total_games = 0
        self.__number = None

    @access_control('username', ADMIN_USERNAME)
    def get_statistics(self) -> None:
        game_time = dt.now() - self.start_time
        print(f'Общее время игры: {game_time}, текущая игра - №{self._total_games}')

    @access_control('username', ADMIN_USERNAME)
    def get_right_answer(self) -> None:
        print(f'Правильный ответ: {self.__number}')

    def check_number(self, guess: int) -> bool:
        # Если число угадано...
        if guess == self.__number:
            print(f'Отличная интуиция, {self.username}! Вы угадали число :)')
            return True

        if guess < self.__number:
            print('Ваше число меньше того, что загадано.')
        else:
            print('Ваше число больше того, что загадано.')
        return False

    def game(self) -> None:
        self.__number = randint(self.MIN_NUM, self.MAX_NUM)
        print(
            '\n'
            f'Угадайте число от {self.MIN_NUM} до {self.MAX_NUM}.'
            '\n'
            'Для выхода из текущей игры введите команду "stop"'
        )
        while True:
            # Получаем пользовательский ввод,
            # отрезаем лишние пробелы и переводим в нижний регистр.
            user_input = input('Введите число или команду: ').strip().lower()

            match user_input:
                case 'stop':
                    break
                case 'stat':
                    self.get_statistics() 
                case 'answer':
                    self.get_right_answer()
                case _:
                    try:
                        guess = int(user_input)
                    except ValueError:
                        print(UNKNOWN_COMMAND)
                        continue

                    if self.check_number(guess):
                        break

    def get_username(self) -> None:
        self.username = input('Представьтесь, пожалуйста, как Вас зовут?\n').strip()
        if self.username == ADMIN_USERNAME:
            print(
                '\nДобро пожаловать, создатель! '
                'Во время игры вам доступны команды "stat", "answer"'
            )
        else:
            print(f'\n{self.username}, добро пожаловать в игру!')


    def guess_number(self) -> None:
        self.get_username()
        self.start_time = dt.now()
        # Счётчик игр в текущей сессии.
        self._total_games = 0
        while True:
            self._total_games += 1
            self.game()
            play_again = input(f'\nХотите сыграть ещё? (yes/no) ')
            if play_again.strip().lower() not in ('y', 'yes'):
                break


if __name__ == '__main__':
    print(
        'Вас приветствует игра "Угадай число"!\n'
        'Для выхода нажмите Ctrl+C'
    )
    game = GuessNumberGame()
    game.guess_number()
