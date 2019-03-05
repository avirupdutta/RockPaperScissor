# rock paper scissors
from random import randint


class CreatePlayer:
    def __init__(self, name=''):
        self.roundScore = 0
        self.name = name

    def won_round(self):
        self.roundScore += 5

def replay():
    loop = True
    print('Want to play again? (Y)es or (N)o')
    while loop:
        try:
            user_input = str(input('--> ')).lower()[0]
            if user_input not in ('y', 'n'):
                raise KeyError
        except KeyError:
            print('Invaid Choice :(')
            print("Enter 'y' for yes and 'n' for no!")
        else:
            loop = False
    if user_input == 'y':
        init()
    else:
        print('~~~~~~~~~    Thanks For Playing      ~~~~~~~~~')
        print('~~~~~~~~~    This game was created by Avirup Dutta      ~~~~~~~~~')
        print('BYE')

def init():
    print('~~~~~~~~~    WELCOME TO ROCK PAPER SCISSOR       ~~~~~~~~~')
    playing = True
    choice_values = ['*', 'rock', 'paper', 'scissor']
    win_score = int(input('Enter max score: '))

    # create players
    player = CreatePlayer(str(input('Enter your name: ')))
    computer = CreatePlayer('Computer')

    # This will display the winning score, round score of the player and round score of computer.
    def display_score():
        print('-------  SCORE BOARD  --------')
        print('Winning score is {}'.format(win_score))
        print('Current score of {} is {}'.format(player.name, player.roundScore))
        print('Current score of {} is {}'.format(computer.name, computer.roundScore))
        print()

    # Displays all the 3 options
    def display_options_to_choose():
        print('===================================================')
        print('Press 1 to choose ROCK')
        print('Press 2 to choose PAPER')
        print('Press 3 to choose SCISSOR')

    # returns either 1,2 or 3 which was entered by the user
    def get_user_choice():
        loop = True

        while loop:
            try:
                user_choice = int(input('--> '))
                if user_choice not in (1, 2, 3):
                    raise ValueError
            except ValueError:
                print('Invalid Choice :(')
                print('Please only enter 1, 2, or 3')
            else:
                loop = False
        return user_choice

    # returns 'p' if player reaches max-score, 'c' when computer reaaches max-score or -1 if no one reaches max-score
    def check_game_win():
        if player.roundScore == win_score:
            return 'p'
        elif computer.roundScore == win_score:
            return 'c'
        else:
            return -1


    # checks game win and round win
    def check_round_win():
        '''
            first checks if anyone has already won...
            -	if won then return (winner, False)
            -	if not won then continue
        '''
        winner = check_game_win()  # Stores either 'p' or 'c' or -1

        if winner in ('p', 'c'):
            return (winner, False)  # This boolean value sets playing variable in while loop.
        else:
            display_options_to_choose()
            player_choose = choice_values[get_user_choice()]
            computer_choose = choice_values[randint(1, 3)]

            # This will display the choises of player and computer
            print('==================')
            print('{}		{}'.format(player.name, computer.name))
            print('{}		{}'.format(player_choose, computer_choose))
            print()

            if player_choose == computer_choose:
                print('This round is TIE! No one scored any points')
                display_score()

            if (player_choose == 'rock' and computer_choose == 'scissor') or (
                    player_choose == 'scissor' and computer_choose == 'paper') or (
                    player_choose == 'paper' and computer_choose == 'rock'):
                print('{} has won the round!'.format(player.name))
                player.won_round()
                display_score()

            elif (computer_choose == 'rock' and player_choose == 'scissor') or (
                    computer_choose == 'scissor' and player_choose == 'paper') or (
                    computer_choose == 'paper' and player_choose == 'rock'):
                print('{} has won the round!'.format(computer.name))
                computer.won_round()
                display_score()

            return (winner, True)  # This boolean value sets playing variable in while loop.

    def declare_winner(winner):

        if winner == 'p':
            winner = player.name
        elif winner == 'c':
            winner = computer.name

        print('*****    =========   ******')
        print('{} has won the GAME!'.format(winner))
        print('*****    =========   ******')

    while playing:

        results = check_round_win()

        if results[0] != -1:
            declare_winner(results[0])
            playing = results[1]

    replay()



# =========================
# Test the functions below:-
# =========================
# display_score()
# display_options_to_choose()
# print(get_user_choice())

init()

# Game Flowchart:-
# ====================
# C -> class
# F -> functions
# V -> global or local variable
# ======================
# choice values -> V
# max score limit -> V
# init -> F
# create players -> C
# display scores -> F
# show options to choose -> F
# get user input -> F
# check round win -> F
# check game win -> F
# declare winner -> F

# replay game -> F
# ==========================