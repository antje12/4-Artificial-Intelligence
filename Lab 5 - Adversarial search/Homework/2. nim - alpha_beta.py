import math

def alpha_beta_decision(state):
    infinity = float('inf')

    def max_value(state, alpha, beta):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for successor in successors_of(state):
            v = max(v, min_value(successor, alpha, beta))
            if v >= beta:
                return v
            alpha = min(alpha, v)
        return v

    def min_value(state, alpha, beta):
        if is_terminal(state):
            return utility_of(state)
        v = infinity

        for successor in successors_of(state):
            v = min(v, max_value(successor, alpha, beta))
            if v <= alpha:
                return v
            beta = max(beta, v)
        return v

    state = argmax(
        successors_of(state),
        lambda a: min_value(a, infinity, -infinity)
    )
    return state


def is_terminal(state):
    # If all piles are of size 1 or 2, there are no more splits to be made
    if (max(state) <= 2):
        return True
    return False


def utility_of(state):
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


def argmax(iterable, func):
    return max(iterable, key=func)


def computer_select_pile(state):
    new_state = alpha_beta_decision(state)
    return new_state


def user_select_pile(list_of_piles):
    '''
    Given a list of piles, asks the user to select a pile and then a split.
    Then returns the new list of piles.
    '''
    list_of_piles.sort(reverse=True)
    print("\n    Current piles: {}".format(list_of_piles))

    i = -1
    while i < 0 or i >= len(list_of_piles) or list_of_piles[i] < 3:
        print("Which pile (from 1 to {}, must be > 2)?".format(len(list_of_piles)))
        i = -1 + int(input())

    print("Selected pile {}".format(list_of_piles[i]))

    max_split = list_of_piles[i] - 1

    j = 0
    while j < 1 or j > max_split or j == list_of_piles[i] - j:
        if list_of_piles[i] % 2 == 0:
            print(
                'How much is the first split (from 1 to {}, but not {})?'.format(
                    max_split,
                    list_of_piles[i] // 2
                )
            )
        else:
            print(
                'How much is the first split (from 1 to {})?'.format(max_split)
            )
        j = int(input())

    k = list_of_piles[i] - j

    new_list_of_piles = list_of_piles[:i] + [j, k] + list_of_piles[i + 1:]

    new_list_of_piles.sort(reverse=True)
    print("    New piles: {}".format(new_list_of_piles))

    return new_list_of_piles


def main():
    state = [20]

    while not is_terminal(state):
        state = user_select_pile(state)
        if not is_terminal(state):
            state = computer_select_pile(state)

    print("    Final state is {}".format(state))

    winner = "Min"
    if (utility_of(state) == 1):
        winner = "Max"
    print("The winner is: " + winner)


if __name__ == '__main__':
    main()
