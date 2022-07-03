def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set([start])  # set of states we have visited
    frontier = [[start]]  # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return Fail


Fail = []

def successors (X, Y):
    def sc(state):
            x, y = state
            assert x <= X and y <= Y
            return {(0, y+x) if y+x <= Y else (x-(Y-y), Y): 'x−>y',
                    (x+y, 0) if x+y <= X else (X, y-(X-x)): 'x<−y',
                    (X, y): 'fill x',
                    (x, Y): 'fill y',
                    (0, y): 'empty x',
                    (x, 0): 'empty y'}
    return sc
if __name__== '__main__':
    res = shortest_path_search ((0, 0), successors (418 , 986) , lambda state: state == (6, 0))
    print(res)
    print('%s transitions' % (int(len(res) / 2)))

