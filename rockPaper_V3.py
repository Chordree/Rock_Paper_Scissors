# check how to implement pygame on pycharm
# just used this code for rock paper scissors instead
#TODO: add various modes of play ... player can be P1 or P2 if one player .. check major diff btw the 3
# add  multi player fuction also ...pwinput function for multiplayers

#TODO: add fuction that will separate inputs based on playmode

# ***********************************************************
#TODO: contribution seprate the main from the scvores ask them to continue playing or different mode 
# look for a code where i have done that ...seem TicTacToe chg**************
import random
import pwinput as pw 
# this is similar to the previous one ... check their major def guess its in a, b calling fuctions 
# *** major diff here is that user input would still be masked on AI mode ***********>>>>delet all uneccessary coments
#  note for this game      r > s,  s > p,  p > r
def play_mode():
    while True:
        try:
            game_mode = input('select (M) for multiplayer or (C) to play against computer: ').strip().upper()

            if game_mode.strip().upper() == 'M':
                var = 'A'
                break
            elif game_mode.strip().upper() == 'C':
                var = 'B'
                break
            if game_mode not in ['M', 'C']:
                continue
        # the code never gets to this except block ... check why
        except AttributeError:
            print('pls enter a valid input, C or M')
            continue
    return var


def human_input():
    user_input = pw.pwinput('enter [r] for Rock, [p] for paper, [s] for scissors:', '#').upper()
    while user_input not in ['R', 'P', 'S']:
        print('you entered an invalid input,.. Valid inputs are r, p, s')
        user_input = pw.pwinput('enter [r] for Rock, [p] for paper, [s] for scissors:', '#').upper()
    return user_input

def ai_input():
    comp_input = random.choice('RPS')  # a list can also be used here
    return comp_input



def check_win(p1, p2):
    if (p1 == 'R' and p2 == 'S') or (p1 == 'S' and p2 == 'P') or (p1 == 'P' and p2 == 'R'):
        return True

def max_score_handler():
    print('set the maximum score for a winner to be declared', 'default max score is 5')
    while True:
        try:
            max_score = int(input('enter a number btw 5 and 15 or any non-numeric key for default maximum score: '))
            if max_score not in range(5, 16):
                print('pls enter a number btw 5 and 15')
                continue
            break
        except ValueError:
            print('*** you entered a non-numeric key, default maximum score activated ***')
            return
            #  this is same as returning None
    return max_score


def main():
    print('rules of the game are >>> R beats S,  S beats P,  P beats R')
    mode = play_mode()
    if mode == 'A':
        p1 = input('player1 enter your name:')
        p2 = input('pls enter your name:')

    if mode == 'B':
        p1 = input('pls enter your name:')
        p2 = 'AI'

    maximum_score = max_score_handler()
    try:
        int(maximum_score)
        print("** you've successfully set the maximum score to be", maximum_score, '**')
        print('the winner would be declared once either of the player reaches', maximum_score)
    except TypeError:
        maximum_score = 5
        print('** default  maximum score is set to 5 **')
        print('the winner would be declared once either of the player reaches', maximum_score)

    # in put a function that would determine the count of where they would stop or 5 if default is selected

    scores_p1, scores_p2 = 0, 0
    switcher = 0
    print('The game starts now. ')
    while scores_p1 < maximum_score and scores_p2 < maximum_score:
        print(f'Round {switcher + 1} ')
           # make this fuction equal to either of the othe two.. see how to set this outside the while loop
        if mode == 'A':
            a, b = human_input(), human_input()
        if mode == 'B':
            a, b = human_input(), ai_input()
        print(a, '***', b)
        if check_win(a, b):
            scores_p1 += 1
            print(p1, 'won this round')
        elif check_win(b, a):
            scores_p2 += 1
            print(p2, 'won this round')
        else:
            print('this round was a tie')
        switcher += 1
        print(f'scoreboard is >>> {p1} {scores_p1} vs {scores_p2} {p2} <<<')

    if scores_p1 > scores_p2:
        print('the winner is', p1)
    else:
        print('the winner is', p2)
    # ask if user wants to continue playing or quit game


    while True:
        replay = input('enter any key to continue or q to quit: ').upper()
        # the upper method above was just used to handle case sensitivity
        if replay != 'Q':
            main()
        break
    # if user wants to switch mode

main()