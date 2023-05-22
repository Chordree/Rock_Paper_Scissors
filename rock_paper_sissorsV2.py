
# add  multi player fuction also ...pwinput function for multiplayers...do this in vscode

# TODO: add fuction that will separate inputs based on playmode... rpexperiment..roc_paper_sis... rpsvv4
import random
import pwinput as pin 
# **** done
# add sleep time for computer 
# add switch mode or continue in present mode statee or quit 

# the major adv is play is masked during multiplayer and opened during single player *********** Major 
#  note for this game      r > s,  s > p,  p > r
def play_mode():
    while True:
        try:
            game_mode = input('select (M) for multiplayer or (C) to play against computer: ').strip().upper()

            if game_mode.strip().upper() == 'M':
                game_play = 'A'
                break

            elif game_mode.strip().upper() == 'C':
                game_play = 'B'
                break

            if game_mode not in ['M', 'C']:
                continue
        # the code never gets to this except block ... check why
        except AttributeError:
            print('pls enter a valid input, C or M')
            continue

    return game_play
    # return value for type of player



def play_multiplayer():
    user_input1 = pin.pwinput('player1 enter [r] for Rock, [p] for paper, [s] for scissors:', '#').upper()
    while user_input1 not in ['R', 'P', 'S']:
        print('you entered an invalid input,.. Valid inputs are r, p, s')
        user_input1 = pin.pwinput('player1 enter [r] for Rock, [p] for paper, [s] for scissors:', '#').upper()

    user_input2 = pin.pwinput('player2 enter [r] for Rock, [p] for paper, [s] for scissors:', '#').upper()
    while user_input2 not in ['R', 'P', 'S']:
        print('you entered an invalid input,.. Valid inputs are r, p, s')
        user_input2 = pin.pwinput('player2 enter [r] for Rock, [p] for paper, [s] for scissors:', '#').upper()

    print(user_input1)
    print(user_input2)
    if user_input1 == user_input2:
        print('this round was a TIE')

    return user_input1, user_input2


def play_ai():
    user_input = input('enter [r] for Rock, [p] for paper, [s] for scissors:').upper()
    while user_input not in ['R', 'P', 'S']:
        print('you entered an invalid input,.. Valid inputs are r, p, s')
        user_input = input('enter [r] for Rock, [p] for paper, [s] for scissors:').upper()

    ai_input = random.choice('RPS')  # a list can also be used here

    print(user_input)
    print(ai_input)
    if user_input == ai_input:
        print('this round was a TIE')

    return user_input, ai_input


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
            print('you entered a non-numeric key, default maximum score activated')
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

    # this function helps determine the count of where they would stop or 5 if default is selected
    maximum_score = max_score_handler()
    try:
        int(maximum_score)
        print("you've successfully set the maximum score to be", maximum_score)
        print('the winner would be declared once either of the player reaches', maximum_score)
    except TypeError:
        maximum_score = 5
        print('default  maximum score is set to 5')
        print('the winner would be declared once either of the player reaches', maximum_score)



    scores_p1, scores_p2 = 0, 0
    switcher = 0
    print('The game starts now. ')
    # see how to  checkmode and set it outside  the while loop to update speed and efficiency
    while scores_p1 < maximum_score and scores_p2 < maximum_score:
        print(f'Round {switcher + 1} ')
        # check a better way to write this.. so it is not checked everytime in the while loop
        if mode == 'A':
            a, b = play_multiplayer()
        # can also use an if condition here also .. used elif to optimize time ..i.e if condition is met skip elif
        elif mode == 'B':
            a, b = play_ai()

        if check_win(a, b):
            scores_p1 += 1
            print(p1, 'won this round')
        if check_win(b, a):
            scores_p2 += 1
            print(p2, 'won this round')

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
#TODO: add a fuctionality that will switch btw reset scores and new game mode ..
# i.e creating a playon function in main would do

main()
