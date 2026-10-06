

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
    level = 0
    frontier = list()
    # 3
    heappush(frontier, (int(h(source)), [source ,level]))
    current_path = ""
    # 2
    while frontier:

     values , path =  heappop(frontier)
     current_path += path[0]
     if limit == path[1] :
         return "reach limit"
     if is_goal(path[0]):
         return current_path
     states = get_successors(path[0])

     for x in states:
           heappush(frontier, (int(h(x)), [x, level +1]))

    return "no solution"
print(dlgreedy("1", 2))