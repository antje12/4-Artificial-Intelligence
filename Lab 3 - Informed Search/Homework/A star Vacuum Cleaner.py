class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0, cost=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.COST = cost

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + \
        ' - Depth: ' + str(self.DEPTH) + \
        ' - Cost: ' + str(self.COST)


'''
Search the tree for the goal state and return path from initial state to goal state
'''
def A_STAR_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_CHEAPEST_NODE(fringe)
        if node.STATE in GOAL_STATES:
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1

        # The cost of getting to my parent + my cost
        s.COST = node.COST + TRAVEL_COST

        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
    queue.append(node)
    return queue


'''
Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    queue.extend(list)
    return queue


'''
Removes and returns the cheapest element from fringe
'''
def REMOVE_CHEAPEST_NODE(queue):
    # Find the cheapest node! f(n) = g(n) + h(n)
    cheapest = None
    for n in queue:
        if cheapest == None:
            cheapest = n
        elif (f(n) < f(cheapest)):
            cheapest = n
    queue.remove(cheapest)
    return cheapest

def f(n):
    return g(n) + h(n)

def g(n):
    # travel cost
    return n.COST

def h(n):
    # heuristic cost
    return H_COST[n.STATE]

'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']


INITIAL_STATE = ('A', 'Dirty', 'Dirty')
GOAL_STATES = {('A', 'Clean', 'Clean'), ('B', 'Clean', 'Clean')}
STATE_SPACE = {('A', 'Dirty', 'Dirty'): [('A', 'Clean', 'Dirty'), ('A', 'Dirty', 'Dirty'), ('B', 'Dirty', 'Dirty')],
               ('A', 'Clean', 'Dirty'): [('A', 'Clean', 'Dirty'), ('A', 'Clean', 'Dirty'), ('B', 'Clean', 'Dirty')],
               ('A', 'Dirty', 'Clean'): [('A', 'Clean', 'Clean'), ('A', 'Dirty', 'Clean'), ('B', 'Dirty', 'Clean')], 
               ('A', 'Clean', 'Clean'): [('A', 'Clean', 'Clean'), ('A', 'Clean', 'Clean'), ('B', 'Clean', 'Clean')],
               ('B', 'Dirty', 'Dirty'): [('B', 'Dirty', 'Clean'), ('A', 'Dirty', 'Dirty'), ('B', 'Dirty', 'Dirty')],
               ('B', 'Clean', 'Dirty'): [('B', 'Clean', 'Clean'), ('A', 'Clean', 'Dirty'), ('B', 'Clean', 'Dirty')],
               ('B', 'Dirty', 'Clean'): [('B', 'Dirty', 'Clean'), ('A', 'Dirty', 'Clean'), ('B', 'Dirty', 'Clean')],
               ('B', 'Clean', 'Clean'): [('B', 'Clean', 'Clean'), ('A', 'Clean', 'Clean'), ('B', 'Clean', 'Clean')]}
# The heuristic function is the amount of dirt left
H_COST = {('A', 'Dirty', 'Dirty'): 3,
          ('A', 'Clean', 'Dirty'): 2,
          ('A', 'Dirty', 'Clean'): 1,
          ('A', 'Clean', 'Clean'): 0,
          ('B', 'Dirty', 'Dirty'): 3,
          ('B', 'Dirty', 'Clean'): 2,
          ('B', 'Clean', 'Dirty'): 1,
          ('B', 'Clean', 'Clean'): 0, }
# You can only travel 1 space, at the cost of 1
TRAVEL_COST = 1


'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = A_STAR_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
