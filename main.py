from program.game import name_players, board_view, \
    turn_input_player, toggle_players, check_win, draw_winner, draw_start_game

""" Tic Tac Toe Game
_____________
dani: O
moshe: X
_____________
| O | 2 | 3 |
_____________
| X | 5 | 6 |
_____________
| O | 8 | 9 |
_____________
Your Choice? [X]: 
"""


def main():
    """
    To start new game
    and check input

    """
    while True:  # start new game
        draw_start_game()
        if input("=: ")[0].upper() != "Y":
            print("Good luck")
            break

        else:
            counter = 0
            name_players()
            board_view()
            print("Game Starting")
            while True:
                turn_input_player()
                board_view()
                toggle_players()
                if check_win() == True:
                    draw_winner()
                    break
                if counter > 8:
                    print("Not any winner")
                    break
                counter += 1


main()
