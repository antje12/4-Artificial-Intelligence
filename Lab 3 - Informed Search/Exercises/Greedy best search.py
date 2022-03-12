class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth

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
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''
def GREEDY_BEST_SEARCH():
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
    # Greedy best first only uses the heuristic function h(n)
    return 0

def h(n):
    # heuristic cost
    return H_COST[n.STATE]

'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']


INITIAL_STATE = 'A'
GOAL_STATES = {'K', 'L'}
STATE_SPACE = {'A': ['B', 'C', 'D'],
               'B': ['F', 'E'], 
               'C': ['E'],
               'D': ['H', 'I', 'J'], 
               'E': ['G', 'H'], 
               'F': ['G'], 
               'G': ['K'],
               'H': ['K', 'L'], 
               'I': ['L'], 
               'J': [], }
H_COST = {'A': 6,
          'B': 5,
          'C': 5,
          'D': 2,
          'E': 4, 
          'F': 5,
          'G': 4,
          'H': 1,
          'I': 2,
          'J': 1,
          'K': 0,
          'L': 0, }


'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = GREEDY_BEST_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
