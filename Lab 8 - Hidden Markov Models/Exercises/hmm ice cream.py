import numpy as np
# pip3 install numpy

"""
Hidden Markov Model using Viterbi algorithm to find most
likely sequence of hidden states.

The problem is to find out the most likely sequence of states
of the weather (hot, cold) from a describtion of the number
of ice cream eaten by a boy in the summer.
"""


def main():
    np.set_printoptions(suppress=True)

    states = np.array(["initial", "hot", "cold", "final"])

    # To simulate starting from index 1, we add a dummy value at index 0
    observationss = [
        [None, 3, 1, 3],
        [None, 3, 3, 1, 1, 2, 2, 3, 1, 3],
        [None, 3, 3, 1, 1, 2, 3, 3, 1, 2],
    ]

    # Markov transition matrix
    # transitions[start, end]
    transitions = np.array([[.0, .8, .2, .0],  # Initial state
                            [.0, .6, .3, .1],  # Hot state
                            [.0, .4, .5, .1],  # Cold state
                            [.0, .0, .0, .0],  # Final state
                            ])

    # P(v|q)
    # emission[state, observation]
    emissions = np.array([[.0, .0, .0, .0],  # Initial state
                          [.0, .2, .4, .4],  # Hot state
                          [.0, .5, .4, .1],  # Cold state
                          [.0, .0, .0, .0],  # Final state
                          ])

    for observations in observationss:
        print("Observations: {}".format(' '.join(map(str, observations[1:]))))

        probability = compute_forward(
            states, observations, transitions, emissions)
        print("Probability: {}".format(probability))

        path = compute_viterbi(states, observations, transitions, emissions)
        print("Path: {}".format(' '.join(path)))

        print('')


# used when making loops instead of standard "in range(a, b):" loops
def inclusive_range(a, b):
    return range(a, b + 1)


def compute_forward(states, observations, transitions, emissions):
    # number of states - subtract two because "initial" and "final" doesn't count.
    big_n = len(states) - 2

    # number of observations - subtract one, because a dummy "None" is added on index 0.
    big_t = len(observations) - 1

    # final state
    f = big_n + 1

    # probability matrix - all values initialized to 5, as 0 has meaning in the matrix
    forward = np.ones((big_n + 2, big_t + 1)) * 5

    '''
    FINISH FUNCITON
    '''

    for state in inclusive_range(1, big_n):
        # start probabilities
        startProbs = transitions[0]
        # the probability of starting in this state
        a = startProbs[state]

        # first observed emission
        o1 = observations[1]

        # this states emissions
        stateEmissions = emissions[state]
        # the probability of the first observation being emissioned in this state
        b = stateEmissions[o1]

        forward[state, 1] = a * b

    for timeStep in inclusive_range(2, big_t):
        # observed emission at this time
        ot = observations[timeStep]

        for state in inclusive_range(1, big_n):
            # this states emissions
            stateEmissions = emissions[state]
            # the probability of the observation being emissioned in this state
            b = stateEmissions[ot]

            sum = 0
            # probability of getting to this state through the previous states
            for sMark in inclusive_range(1, big_n):

                # probabilities of going from previous state
                prevProbs = transitions[sMark]
                # the probability of getting to this state
                a = prevProbs[state]

                # the probability of getting to this state
                # through the previous state (prob of getting to that state)
                # and observing the emission in this state
                sum += forward[sMark, timeStep-1] * a * b

            forward[state, timeStep] = sum

    sum = 0
    # probability of getting to the final state through the previous states
    for state in inclusive_range(1, big_n):
        # probabilities of going from previous state
        prevProbs = transitions[state]
        # the probability of getting to this state
        a = prevProbs[f]

        # the probability of getting to this state
        # through the previous state (prob of getting to that state)
        sum += forward[state, big_t] * a

    forward[f, big_t] = sum

    # return the probability of the final state
    return forward[f, big_t]


def compute_viterbi(states, observations, transitions, emissions):
    # number of states - subtract two because "initial" and "final" doesn't count.
    big_n = len(states) - 2

    # number of observations - subtract one, because a dummy "None" is added on index 0.
    big_t = len(observations) - 1

    # final state
    f = big_n + 1

    # probability matrix - all values initialized to 5, as 0 is valid value in matrix
    viterbi = np.ones((big_n + 2, big_t + 1)) * 5

    # Must be of type int, otherwise it is tricky to use its elements to index
    # the states
    # all values initialized to 5, as 0 is valid value in matrix
    backpointers = np.ones((big_n + 2, big_t + 1), dtype=int) * 5

    '''
    FINISH FUNCTION
    '''

    for state in inclusive_range(1, big_n):
        # start probabilities
        startProbs = transitions[0]
        # the probability of starting in this state
        a = startProbs[state]

        # first observed emission
        o1 = observations[1]

        # this states emissions
        stateEmissions = emissions[state]
        # the probability of the first observation being emissioned in this state
        b = stateEmissions[o1]

        viterbi[state, 1] = a * b
        backpointers[state, 1] = 0

    for timeStep in inclusive_range(2, big_t):
        for state in inclusive_range(1, big_n):

            # observed emission at this time
            ot = observations[timeStep]

            # this states emissions
            stateEmissions = emissions[state]
            # the probability of the observation being emissioned in this state
            b = stateEmissions[ot]

            values = []
            # probability of getting to this state through the previous states
            for sMark in inclusive_range(1, big_n):

                # probabilities of going from previous state
                prevProbs = transitions[sMark]
                # the probability of getting to this state
                a = prevProbs[state]

                # the probability of getting to this state
                # through the previous state (prob of getting to that state)
                # and observing the emission in this state
                values.append(viterbi[sMark, timeStep-1] * a * b)

            # save the max probability
            viterbi[state, timeStep] = max(values)
            # save the backpointer index
            backpointers[state, timeStep] = argmax(values)

    values = []
    # probability of getting to the final state through the previous states
    for state in inclusive_range(1, big_n):
        # probabilities of going from previous state
        prevProbs = transitions[state]
        # the probability of getting to this state
        a = prevProbs[f]

        # the probability of getting to this state
        # through the previous state (prob of getting to that state)
        values.append(viterbi[state, big_t] * a)

    # save the max probability
    viterbi[f, big_t] = max(values)
    # save the backpointer index
    backpointers[f, big_t] = argmax(values)

    print(backpointers)

    # return the backtrace path by following backpointers
    # to states back in time from backpointer[f, T]
    path = []

    state = f
    time = big_t

    # append the last state (the state of the last day)
    path.append(states[backpointers[state, time]])
    state = backpointers[f, time]

    # move back in time
    while (0 < time):

        if (0 < backpointers[state, time]):
            path.append(states[backpointers[state, time]])

        state = backpointers[state, time]
        time -= 1

    # reverse the output to get the days in correct order
    path.reverse()
    return path


def argmax(sequence):
    # Note: You could use np.argmax(sequence), but only if sequence is a list.
    # If it is a generator, first convert it: np.argmax(list(sequence))

    # Since we loop from 1 to big_n, the result of argmax is between
    # 0 and big_n - 1. However, 0 is the initial state, the actual
    # states start from 1, so we add 1.
    return 1 + max(enumerate(sequence), key=lambda x: x[1])[0]


if __name__ == '__main__':
    main()
