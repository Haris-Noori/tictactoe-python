# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def print_board(xState, zState):
    print(f"=============")
    print(f"| 0 | 1 | 2 |")
    print(f"=============")
    print(f"| 3 | 4 | 5 |")
    print(f"=============")
    print(f"| 6 | 7 | 8 |")
    print(f"=============")


def main():
    xState = [0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0]
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