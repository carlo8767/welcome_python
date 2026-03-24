### Please provide the answer to Question 1 here, as a python comment
#
# WHAT HAPPENS IF GREED SEARCH HAVE THE SAME HERISTICH FUNCTION ? DBS OR BFR
#
#
#
#
#
#


### Question 2

import heapq as hp

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
    count_limit = 0
    store_path = list()

    list_test = list()
    next_edge = list(source)[0]
    store_path.append(next_edge)
    while True:
        edges = source[next_edge]
        if edges == []:
            return store_path
        for s in edges:
            cost_heuristich = h(s)

            # dict_cost[s]= cost_heuristich
            # list_cost.append((s,cost_heuristich))
            hp.heappush(list_test, cost_heuristich)
        count_limit += 1
        least_cost = hp.heappop(list_test)
        # VERIFY IF THE COST IS
        if least_cost == 0:
            return next_edge
        for k in heuristic_values.keys():
            values = heuristic_values[k]
            if values == least_cost:
                next_edge = k
                break
        store_path.append(next_edge)
        if count_limit == limit:
            break
        list_test.clear()
        print(edges)
    return next_edge


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
dlgreedy(graph, 2)

