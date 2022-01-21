from search import *

if __name__ == '__main__':

    initial_state = (1, 2, 3, 4, 5, 7, 8, 6, 0)
    eight_puzzle = EightPuzzle(initial_state)
    path = breadth_first_graph_search(eight_puzzle).solution()
    
    zeroIndex = 8

    stateArray = [1, 2, 3, 4, 5, 7, 8, 6, 0]

    for item in path:
        print(stateArray)
        if (item == "LEFT"):
            prevIndex = zeroIndex
            zeroIndex = zeroIndex - 1

            otherNumber = stateArray[zeroIndex]

            stateArray[zeroIndex] = 0
            stateArray[prevIndex] = otherNumber
        elif (item == 'RIGHT'):
            prevIndex = zeroIndex
            zeroIndex = zeroIndex + 1

            otherNumber = stateArray[zeroIndex]

            stateArray[zeroIndex] = 0
            stateArray[prevIndex] = otherNumber
        elif (item == 'UP'):
            prevIndex = zeroIndex
            zeroIndex = zeroIndex - 3

            otherNumber = stateArray[zeroIndex]

            stateArray[zeroIndex] = 0
            stateArray[prevIndex] = otherNumber
        elif (item == 'DOWN'):
            prevIndex = zeroIndex
            zeroIndex = zeroIndex + 3

            otherNumber = stateArray[zeroIndex]

            stateArray[zeroIndex] = 0
            stateArray[prevIndex] = otherNumber

    print(stateArray)