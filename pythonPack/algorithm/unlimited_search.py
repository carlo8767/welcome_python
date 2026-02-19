# function returning the last state of a path
def get_last_state(path):
    if path != []:
        return path[-1]
    return []


# function returning the successor of a state # generate all the possible combinations
def get_successors(state):
    successors = []
    for i in range(0, len(state) - 1):
        for j in range(i, len(state)):
            new_state = state[:]
            tmp = new_state[i]
            new_state[i] = new_state[j]
            new_state[j] = tmp
            successors += [new_state]
    return successors


# function checking whether an array is in acending order
def is_ascending(state):
    for i in range(0, len(state) - 1):
        if state[i] > state[i + 1]:
            return False
    return True


# function checking whether an array is in acending order
def is_ascending_order(state):
    verify = state.copy()
    if verify.sort() == state:
            return True
    else:
            return False


# function checking whether an array is in descending order
def is_descending(state):
    for i in range(0, len(state) - 1):
        if state[i] < state[i + 1]:
            return False
    return True

# function checking whether an array is in descending order
def is_descending_order(state):
    verify = state.copy()
    if verify.sort(reversed=True) == state:
        return True
    else:
        return False

# function checking whether an array is a goal state
def is_goal(state):
    return is_ascending(state) or is_descending(state)


# implementation of depth limited search
def dls(source, limit):
    frontier = [[source]]
    max_paths = len(frontier)
    while frontier != []:

        path, frontier = frontier[0], frontier[1:]

        last_state = get_last_state(path)

        if is_goal(last_state):
            return path

        if len(path) <= limit:
            # GENERATES ALL POSSIBLE COMBINATIONS
            successors = get_successors(last_state)
            for s in successors:
                frontier = [path + [s]] + frontier

    return []


# implementation of iterative deepening search
def ids(source):
    limit = 0
    path = []
    while path == []:
        path = dls(source, limit)
        limit += 1
    return path


# a simple test
path = ids([2,3,1,6,4,5])

for step, state in enumerate(path):
    print("Step", step, ":", state)