A = 'A'
B = 'B'
Environment = {
    A: "Dirty",
    B: "Dirty",
    "Current": A
}

# determine action
def REFLEX_VACCUM_AGENT(loc_st):
    if loc_st[1] == "Dirty":
        return "Suck"
    if loc_st[0] == A:
        return "Right"
    if loc_st[0] == B:
        return "Left"

# sense environment
def Sensors():
    location = Environment["Current"]
    return (location, Environment[location])

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
run(10, REFLEX_VACCUM_AGENT)
