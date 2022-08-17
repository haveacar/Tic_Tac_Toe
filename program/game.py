import time

current_player = 1
player_first_name = "Player 1"
player_second_name = "Player 2"
board = list(range(1, 10))
turn = "O"
win_comp = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
player_win = "Player"


def name_players():
    """
    Func input name of players
    """
    global player_first_name, player_second_name
    player_first_name = input("First player name :")
    player_second_name = input("Second player name :")


def toggle_players():
    """
    Toggle players player 1 or 2
    """
    global current_player, turn, player_win
    if current_player == 1:
        current_player = 2
        turn = "X"  # player 2 turn
        player_win = player_second_name  # winner first player
        pass
    else:
        current_player = 1
        turn = "O"  # player 1 turn
        player_win = player_first_name  # winner second player
        pass


def board_view():
    """
    Func to draw board 3X3,
    players
    :return:
    """
    line = "_____________"

    print(f"{line}\n{player_first_name}: O\n{player_second_name}: X\n{line}")  # to print players name
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")  # draw board
        print(line)


def turn_input_player():
    """
    Func check input isdigit, range, or free space.
    And write player turn
    :return:
    """

    while True:
        player_turn = input(f"Your Choice? [{turn}]: ")
        if not player_turn.isdigit() or int(player_turn) not in range(1, 10):  # check digit input and range
            print("Wrong input")
            continue
        player_turn = int(player_turn)
        if board[player_turn - 1] == "X" or board[player_turn - 1] == "O":  # check or is free
            print("Not free")
            continue
        board[player_turn - 1] = turn
        break


def check_win():
    """
    check winner combination
    :return:
    """
    for i in win_comp:  # if winner return True
        if board[i[0] - 1] == board[i[1] - 1] == board[i[2] - 1]:
            return True

    else:
        return False


def draw_winner():
    """
    func print winner and score
    :return:
    """
    star_line = len(player_win) * "*"
    print(f"{star_line}\n*WIN!:*  \n{star_line}")
    for i in range(len(player_win)):
        time.sleep(0.1)
        print(player_win[i], end="")
    print(f"\n{star_line}")
    pass


def draw_start_game():
    """
    func to draw star new game
    :return:
    """

    start_mess = "Start New Game [Y] or [Any key to break]?"
    star_line = len(start_mess) * "*"
    print(f"\n{star_line}")
    for j in range(len(start_mess)):
        time.sleep(0.1)
        print(start_mess[j], end="")
    print(f"\n{star_line}")
