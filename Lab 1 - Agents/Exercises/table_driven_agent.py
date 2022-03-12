A = 'A'
B = 'B'
percepts = []
table = {
    ((A, "Clean"),): "Right",
    ((A, "Dirty"),): "Suck",
    ((B, "Clean"),): "Left",
    ((B, "Dirty"),): "Suck",
    ((A, "Clean"), (A, "Clean")): "Right",
    ((A, "Clean"), (A, "Dirty")): "Suck",
    # ...
    ((A, "Clean"), (A, "Clean"), (A, "Clean")): "Right",
    ((A, "Clean"), (A, "Clean"), (A, "Dirty")): "Suck",
    ((A, "Clean"), (A, "Dirty"), (B, "Clean")): "Left",
    # ...
}

def LOOKUP(percepts, table): 
    # lookup appropriate action for percepts
    action = table.get(tuple(percepts))
    return action

# determine action based on table and percepts
def TABLE_DRIVEN_AGENT(percept):
    # add percept
    percepts.append(percept) 
    # lookup appropriate action for percepts
    action = LOOKUP(percepts, table)
    return action

# run agent on several sequential percepts
def run():
    print("Action\tPercepts")
    print(TABLE_DRIVEN_AGENT(((A, "Clean"))), '\t', percepts)
    print(TABLE_DRIVEN_AGENT(((A, "Dirty"))), '\t', percepts)
    print(TABLE_DRIVEN_AGENT(((B, "Clean"))), '\t', percepts)

# new code    
run()
print(TABLE_DRIVEN_AGENT(((B, "Clean"))), '\t', percepts)
