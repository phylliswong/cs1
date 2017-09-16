# Take a bet
# bet takes color
# bet takes number
# bet takes bet amount

# spin the wheel - generate the number
# random module rand.int
# check the result - did the bet match the result of the spin
# if win - pay accordingly
# if loss - keep money

# functions should do one thing only!!!!
import random
random.seed(1)

bank_account = 1000
bet_amount = 0
bet_color = None
bet_num = None

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

def take_bet(color, number, amount):
    total_bet = []
    total_bet.append(color)
    total_bet.append(number)
    total_bet.append(amount)
    return total_bet

def roll_ball():
    '''returns a random number between 0 and 37'''
    results = []
    ball_num = random.randint(0, 37)
    if (ball_num in green):
        results.append('green')
    elif (ball_num in red):
        results.append('red')
    elif (ball_num in black):
        results.append('black')
    results.append(ball_num)
    return results

def check_results():
    '''Compares bet_color to color rolled.  Compares
    bet_number to number_rolled.'''
    pass

def payout():
    '''returns total amount won or lost by user based on results of roll. '''
    pass

def play_game():
    """This is the main function for the game.
    When this function is called, one full iteration of roulette,
    including:
    Take the user's bet.
    Roll the ball.
    Determine if the user won or lost.
    Pay or deduct money from the user accordingly.
    """
    pass