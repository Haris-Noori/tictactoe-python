# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def print_board(xState, zState):
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


def main():
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]
    turn = 1    # 1 for X and 0 for O

    print("*** WELCOME TO TIC TAC TOE GAME ***")
    
    while(True):
        print_board(xState, zState)
        if(turn == 1):
            print("X's chance")
            value = int(input("Enter value: "))
            xState[value] = 1
        
        else:
            print("X's chance")
            value = int(input("Enter value: "))
            zState[value] = 1

main()