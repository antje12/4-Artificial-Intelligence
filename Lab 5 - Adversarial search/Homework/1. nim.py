import math

def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for s in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for s in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    state = argmax(successors_of(state), lambda a: min_value(a))
    return state


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """

    # If all piles are of size 1 or 2, there are no more splits to be made
    if (max(state) <= 2):
        return True

    return False


def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """

    number_of_piles = len(state)

    # Min first move = 2 piles (even)
    # Max first move = 3 piles (uneven)
    if (number_of_piles % 2) == 0:
        # Min made the last move and won
        return -1
    else:
        # Max made the last move and won
        return 1

    return 0


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """

    successors = []
    
    # check every pile
    for i in range(0, len(state)):
        pile_value = state[i]
        # if it is splittable we can create successors
        if pile_value > 2:
            p1 = pile_value-1
            p2 = 1

            max = math.ceil(pile_value/2)-1
            while p2 <= max:
                s = list.copy(state)
                s[i] = p1
                s.append(p2)
                split_state = (i, s)
                successors.append(s)
                p1 = p1-1
                p2 = p2+1

    return successors


def display(state):
    state.sort(reverse=True)
    print("Piles:")
    print(*state, sep = ", ")


def main():
    board = [15]
    while not is_terminal(board):
        # Min turn
        display(board)
        index = int(input('What pile to split? '))
        take = int(input('How many do you take? '))

        start = board[index-1]
        board[index-1] = start-take
        board.append(take)

        if not is_terminal(board):
            # Max turn
            board = minmax_decision(board)

    display(board)

    winner = "Min"
    if (utility_of(board) == 1):
        winner = "Max"
    print("The winner is: " + winner)    


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
