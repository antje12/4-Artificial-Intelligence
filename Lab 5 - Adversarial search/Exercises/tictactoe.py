def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """

    # check for tie (board full)
    xCount = state.count("X")
    oCount = state.count("O")
    if xCount + oCount == 9:
        return True

    # check for win: there are 8 winning combinations
    if state[0] == state[1] == state[2] or \
        state[3] == state[4] == state[5] or \
        state[6] == state[7] == state[8] or \
        state[0] == state[3] == state[6] or \
        state[1] == state[4] == state[7] or \
        state[2] == state[5] == state[8] or \
        state[0] == state[4] == state[8] or \
        state[2] == state[4] == state[6]:
        return True

    return False


def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """

    xCount = state.count("X")
    oCount = state.count("O")

    # there cannot be a tie if the board is unfilled
    if xCount + oCount != 9:
        if xCount == oCount:
            # O made last move and won
            return -1
        else:
            # X made last move and won
            return 1
    
    # check if we have a winner or a tie
    # if there is a winner, and the board is full, it has to be X
    if state[0] == state[1] == state[2] or \
        state[3] == state[4] == state[5] or \
        state[6] == state[7] == state[8] or \
        state[0] == state[3] == state[6] or \
        state[1] == state[4] == state[7] or \
        state[2] == state[5] == state[8] or \
        state[0] == state[4] == state[8] or \
        state[2] == state[4] == state[6]:
        return 1

    return 0


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """

    successors = []
    player_token = ""

    xCount = state.count("X")
    oCount = state.count("O")

    if xCount == oCount:
        # X's turn
        player_token = "X"
    else:
        # O's turn
        player_token = "O"
    
    # check every field
    for i in state:
        # if it is empty we can make a move by placing a token
        if i != "X" and i != "O":
            s = list.copy(state)
            s[i] = player_token
            moveState = (i, s)
            successors.append(moveState)

    return successors


def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
