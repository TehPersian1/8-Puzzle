from search import *

def printTable(stateArray):

        print(stateArray[0], stateArray[1], stateArray[2])
        print(stateArray[3], stateArray[4], stateArray[5])
        print(stateArray[6], stateArray[7], stateArray[8])
        print()
     

if __name__ == '__main__':

    initial_state = (1, 2, 3, 4, 5, 7, 8, 6, 0)
    eight_puzzle = EightPuzzle(initial_state)
    path = breadth_first_graph_search(eight_puzzle).solution()
    
    zeroIndex = 8

    stateArray = [1, 2, 3, 4, 5, 7, 8, 6, 0]

    for item in path:
        #print(stateArray)

        printArray = stateArray
        printArray.remove(0)
        printArray.insert(zeroIndex, ' ')

        printTable(printArray)
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
    
    printArray = stateArray
    printArray.remove(0)
    printArray.insert(zeroIndex, ' ')
    printTable(printArray)