A = 'A'
B = 'B'
state = {}
action = None
# initially ignorant
model = {A: None, B: None}
RULE_ACTION = {
    1: 'Suck',
    2: 'Right',
    3: 'Left',
    4: 'NoOp'
}
# ex. rule (if location == A && Dirty then action 1)
rules = {
    (A, 'Dirty'): 1,
    (B, 'Dirty'): 1,
    (A, 'Clean'): 2,
    (B, 'Clean'): 3,
    (A, B, 'Clean'): 4
}
Environment = {
    A: 'Dirty',
    B: 'Dirty',
    "Current": A
}

 # no interpretation
def INTERPRET_INPUT (input):
    return input

# match rule for a given state
def RULE_MATCH(state, rules): 
    rule = rules.get(tuple(state))
    return rule

def UPDATE_STATE(state, action, percept):
    (location, status) = percept
    state = percept
    if model[A] == model[B] == "Clean":
        # model consulted only for A and B Clean
        state = (A, B, "Clean")
    # update the model state
    model[location] = status
    return state

# determine action
def REFLEX_AGENT_WITH_STATE(percept):
    global state, action
    state = UPDATE_STATE(state, action, percept)
    rule = RULE_MATCH(state, rules)
    action = RULE_ACTION[rule]
    return action

# sense environment
def Sensors():
    location = Environment["Current"]
    return(location, Environment[location])

# modify environment
def Actuators(action):
    location = Environment["Current"]
    if action == "Suck":
        Environment[location] = "Clean"
    elif action == "Right" and location == A:
        Environment["Current"] = B
    elif action == "Left" and location == B:
        Environment["Current"] = A

# run the agent through n steps
def run (n, make_agent):
    print("Current:                 New:")
    print("location status  action  location    status")
    for i in range(0, n):
        # sense environment before action
        (location, status) = Sensors()
        print("{:9s}{:8s}".format(location, status), end='')

        # do action on environment
        action = make_agent(Sensors())
        Actuators(action)

        # sense environment after action
        (location, status) = Sensors()
        print("{:8s}{:12s}{:8s}".format(action, location, status))

# new code
run(10, REFLEX_AGENT_WITH_STATE)
