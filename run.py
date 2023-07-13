def sum(a, b, c):
    """ to overwrite the function of sum in python,
    to check if any pattern matched to win the game """
    return a + b + c


def print_board(xState, zState):
    """ takes both states, and print the board on the console """

    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)

    print(f"=============")
    print(f"| {zero} | {one} | {two} |")
    print(f"=============")
    print(f"| {three} | {four} | {five} |")
    print(f"=============")
    print(f"| {six} | {seven} | {eight} |")
    print(f"=============")


def check_win(xState, zState):
    """ takes both the states, and check each time
    if any of the player has managed to win the game or not """

    xWins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for win in xWins:
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print_board(xState, zState)
            print(f"X won the match ;)")
            return 1
        if (sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print_board(xState, zState)
            print(f"O won the match ;)")
            return 0

    return -1


def start_game():
    """ Displays the intro message, and take inputs from the players,
    check the datatype and pass to next functions  """

    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1    # 1 for X and 0 for O

    print("*** WELCOME TO TIC TAC TOE GAME ***")

    while (True):
        print_board(xState, zState)
        if (turn == 1):
            print(f"")
            print("X's chance")

            try:
                value = int(input("Enter value: "))
                if (value >= 0 and value <= 8):
                    if xState[value] == 1:
                        print(f"[Error] Already Marked")
                        turn = 0
                    else:
                        xState[value] = 1
                else:
                    print(f"[Error] Please input numbers from 0 to 8")
                    turn = 0

            except ValueError:
                print(f"[Error] Please input numbers from 0 to 8")
                turn = 0

        else:
            print(f"")
            print("O's chance")

            try:
                value = int(input("Enter value: "))
                if (value >= 0 and value <= 8):
                    if (zState[value] == 1):
                        print(f"[Error] Already Marked")
                        turn = 1
                    else:
                        zState[value] = 1
                else:
                    print(f"[Error] Please input numbers from 0 to 8")
                    turn = 1

            except ValueError:
                print(f"[Error] Please input numbers from 0 to 8")
                turn = 1

        cwin = check_win(xState, zState)
        if (cwin != -1):
            print(f"*** Match Over ***")
            break

        turn = 1 - turn


def main():
    """ Starts the game function """

    start_game()


main()
