
"""
any
all
next
list_result = [x for x in data if condition]
for k, value in dictionary.items():
pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
zip
extend, join, copy
union_messages = verify_relation(relations, lambda a, b: a | b, "is UNION of")
"""



# simple representation of the graph on the exercise sheet
# every key of the dictionary is a node and its value is the list of successors
#
my_graph = {"a":["b", "c", "d"], "b": ["e"], "c":["e"], "d":["e"], "e":["f"]}


# a simple function to get the last state of a path
# assuming the path is just a string and the last state is the last character
def get_last_state(path):
    return path[-1]

# simple utility function returnes edges
def get_successors(a_graph, state):
    if state in a_graph.keys():
        return a_graph[state]
    return []


# breadth-first traversal
def breadth(a_graph, source_node):
    visited = []
    to_visit = [source_node]
    while to_visit != []:
        node, to_visit = to_visit[0], to_visit[1:]
        if node not in visited:
            visited += [node]
            to_visit += get_successors(a_graph, node);
    return visited


# depth-first traversal
def depth(a_graph, source_node):
    visited = []
    to_visit = [source_node]
    while to_visit != []:
        node, to_visit = to_visit[0], to_visit[1:]
        if node not in visited:
            visited += [node]
            to_visit = get_successors(a_graph, node) + to_visit;
    return visited



# uncomment the following line and implement breadth-first search

def breadth_search(a_graph, source, destination):
    queue_edge = []
    path_destination = [source]
    source_key_node= [source]
    while source_key_node :
        if source_key_node [0] == destination:
            return path_destination
        queue_edge += breadth_extract_edges(a_graph, source_key_node[0])
        source_key_node , queue_edge = queue_edge[0], queue_edge[1:]
        path_destination += source_key_node
    return  path_destination


def breadth_extract_edges (a_graph, source_key):
    if source_key in a_graph.keys():
       return a_graph[source_key]
    return []


# uncomment the following line and implement depth-first search
def depth_search(a_graph, source, destination):
    stack_edge = []
    path_visited = [source]
    source_key_node = [source]
    while source_key_node:
        stack_edge += depth_search_depth(a_graph, source_key_node[0])
        if  not stack_edge :
            return path_visited
        source_key_node = stack_edge[-1:]
        stack_edge = stack_edge[:-1]
        if source_key_node not in path_visited:
            path_visited += source_key_node
        if source_key_node[0] == destination:
            return path_visited
    return path_visited


def depth_search_depth (a_graph, source_key):
    if source_key in a_graph.keys():
       verify = a_graph[source_key]
       verify.copy().reverse()
       return verify
    return []






if __name__ == '__main__':



    elements = ['a', 'b', 'caa']
    ts = elements[:-1]
    print(elements[-1])


    visited_breath_traverse = breadth(my_graph, "a")
    visited_depth_traverse =  depth(my_graph, "a")
    print(visited_breath_traverse)
    print(visited_depth_traverse)

    path = breadth_search(my_graph, "a", "c")
    print(f'the path is {path}')
    graph = {
        'A': ['BB'],
        'BB': ['C'],
        'C': []
    }

    print(depth_search(graph, 'A', 'C'))