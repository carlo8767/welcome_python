### Please provide the answer to Question 1 here, as a python comment
#
#
#
#
#
#
#
#


### Question 2

from heapq import heappush, heappop

graph = {
    '1': ['2', '3', '9'],
    '2': ['4', '5'],
    '3': ['4', '5'],
    '4': ['6', '7', '8'],
    '5': ['6', '7', '8'],
    '6': [],
    '7': [],
    '8': [],
    '9': ['8']
}

heuristic_values = {
    '1': 10,
    '2': 8,
    '3': 9,
    '4': 0,
    '5': 6,
    '6': 5,
    '7': 4,
    '8': 3,
    '9': 6
}


# function returning the last state of a path
def get_last_state(path):
    if path != []:
        return path[-1]
    return []


# function returning the successor of a state
def get_successors(state):
    successors = graph[state]
    return successors


# function returning the heuristic estimate distance to target
def h(state):
    return heuristic_values[state]


# function checking whether an array is a goal state
# recall that the heuristic has to be equal to 0 for all goal states
def is_goal(state):
    return heuristic_values[state] == 0


# implementation of greedy search
def dlgreedy(source, limit):
    # 3 marks
    frontier = []
    heappush(frontier, (h(source), [source]))

    # 2 marks
    while frontier != []:

        # 5 marks
        path = heappop(frontier)[1]

        last_state = get_last_state(path)

        # 3 marks
        if is_goal(last_state):
            return path

            # 3 marks
        if len(path) < limit:
            # 5 marks
            successors = get_successors(last_state)
            for s in successors:
                heappush(frontier, (h(s), path + [s]))

    # 2 marks
    return []


print(dlgreedy('1', 3))