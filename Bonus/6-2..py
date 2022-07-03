x_missionaries = 3
x_cannibals = 3
y_missionaries = 0
y_cannibals = 0


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


def move(missionary, number, from_where):
    global x_missionaries
    global y_missionaries
    global x_cannibals
    global y_cannibals
    
    if(missionary == "both"):
        if from_where == "x" and x_missionaries > 0 and x_cannibals > 0:
            x_missionaries -= 1
            x_cannibals -= 1
            y_missionaries += 1
            y_missionaries += 1
        elif x_missionaries > 0 and x_cannibals > 0:
            y_missionaries -= 1
            y_cannibals -= 1
            x_missionaries += 1
            x_missionaries += 1
            
    
    if(missionary):
        if from_where == "x" and x_missionaries > 0:
            x_missionaries -= 1
            y_missionaries += 1
        elif y_missionaries > 0:
            y_missionaries -= 1
            x_missionaries += 1
    else:
        if from_where == "x" and x_cannibals > 0:
            x_cannibals -= 1
            y_cannibals += 1
        elif y_cannibals > 0:
            y_cannibals -= 1
            x_cannibals += 1
    return(x_missionaries + x_cannibals, y_missionaries + y_cannibals)


def successors(X, Y):
    def sc(state):
        global x_missionaries
        global y_missionaries
        global x_cannibals
        global y_cannibals
        x = x_missionaries+x_cannibals
        y = y_missionaries+y_cannibals
        x, y = state
        assert y_missionaries <= X and y_missionaries <= Y
        return {move(True, 1, "x") if (x_cannibals  <= x_missionaries -1 and y_cannibals <= y_missionaries+1) else (x,y): '' ,
                move(True, 2, "x") if (x_cannibals <= x_missionaries -2 and y_cannibals <= y_missionaries+2)else (x,y): '' ,
                move(True, 1, "y") if (y_cannibals  <= y_missionaries -1 and x_cannibals <= x_missionaries+1)else (x,y): '' ,
                move(True, 2, "y") if (y_cannibals <= y_missionaries -2 and x_cannibals <= x_missionaries+2)else (x,y): '',
                move(False, 1, "x") if (x_cannibals-1  <= x_missionaries  and y_cannibals+1 <= y_missionaries) else (x,y): '' ,
                move(False, 2, "x") if (x_cannibals <= x_missionaries -2 and y_cannibals+2 <= y_missionaries)else (x,y): '' ,
                move(False, 1, "y") if (y_cannibals-1  <= y_missionaries and x_cannibals+1 <= x_missionaries)else (x,y): '' ,
                move(False, 2, "y") if (y_cannibals-2 <= y_missionaries and x_cannibals+2 <= x_missionaries)else (x,y): '',
                move("both", 2, "y") if (x,y)else (x,y): '',
                }
    return sc


if __name__ == '__main__':
    res = shortest_path_search((6, 0), successors(x_cannibals, y_cannibals), lambda state: state == (0, 6))
    print(res)
    print('%s transitions' % (int(len(res) / 2)))
