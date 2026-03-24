import heapq

heuristic_values = {
    '1': 10,
    '2': 8,
    '3': 9,
    '4': 0,
    '5': 6,
    '6': 5,
    '7': 4,
    '8': 3,
    '9': 6}

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


# function returning the successor of a state
def get_successors(state):
    successors = graph[state]
    return successors

def heuristich (x):
    return  heuristic_values[x]

# function checking whether an array is a goal state
# recall that the heuristic has to be equal to 0 for all goal states
def is_goal(state):
    return heuristic_values[state] == 0


def greedy(source):
    list_path = list()
    heapq.heappush(list_path,(heuristich(source), source))
    while list_path:
        c, n = heapq.heappop(list_path)
        path = n
        edges = get_successors(n[-1])
        for x in edges:
             hc = heuristich(x)
             path += x
             heapq.heappush(list_path,(hc,path))
             if is_goal(x):
                 return path

    return []


print(greedy('1'))