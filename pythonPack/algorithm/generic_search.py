import heapq

set_state = {"Berlin": "München", "München":"Lipsia" ,"Koln":"Dresden"}
goal_state = "Dresden"

def generic_search (input_state):
    nodes =   [k for k, v in set_state.items() if k is not input_state]
    frontier = [input_state]
    while frontier :
        verify_state =  frontier.pop(0)
        verify_goal = set_state[verify_state] == goal_state
        if verify_goal:
            return "Find path"
        else :
            frontier.append(nodes.pop(0))
    return "not find"

print(generic_search("Berlin"))



graph_states = {"S": ["C", "B","A"], "A":["D","E"] ,"B":["G"] ,"C":["F"], "D": ["H"], "E": ["G"], "G": ["F"] , "F": [] , "H" : []}
goal_states = ("G")
def breadth_first(initial_state):
    frontier = list()
    frontier.append(initial_state)
    while frontier:
        # FOR BFS THE FIRST IS FIFO
        pre = frontier.pop(0)
        for edges in graph_states[pre[-1]]:
            pre+=edges
            if goal_states in pre:
                return pre
            frontier.append(pre)
            pre = pre.replace(edges, "")
    return "Not find"
print(breadth_first("S"))



def depth_first(initial_state):
    frontier = list()
    frontier.append(initial_state)
    while frontier:
        # FOR DFS THE FIRST IS LIFO
        pre = frontier.pop(-1)
        for edges in graph_states[pre[-1]]:
            pre+=edges
            if goal_states in pre:
                return pre
            frontier.append(pre)
            pre = pre.replace(edges, "")
    return "Not find"

print(depth_first("S"))

# graph_states = {"S": ["C", "B","A"], "A":["D","E"] ,"B":["G"] ,"C":["F"], "D": ["H"], "E": ["G"], "G": ["F"] , "F": [] , "H" : []}

def depth_first_limit(initial_state, limit):
    frontier = list()
    count_limit = 0
    frontier.append((initial_state, count_limit))
    while frontier:
        pre , lim_check = frontier.pop(-1)
        if  lim_check == limit and not frontier:
            return "Reach limit"
        elif  lim_check == limit:
                continue
        for edges in graph_states[pre[-1]]:
            pre+=edges
            if goal_states in pre:
                return pre
            frontier.append((pre,count_limit+1))
            pre = pre.replace(edges, "")
        count_limit+=1


    return "Not find"

print(depth_first_limit("S", 2))


def depth_first_limit_o(initial_state, goal_state, limit):
    # Stack: (current_node, path, depth)
    frontier = [(initial_state, [initial_state], 0)]

    while frontier:
        node, path, depth = frontier.pop()

        # Goal check
        if node == goal_state:
            return path

        # Depth limit check
        if depth == limit:
            continue

        # Expand neighbors
        for neighbor in graph_states[node]:
            if neighbor not in path:  # avoid cycles
                new_path = path + [neighbor]
                frontier.append((neighbor, new_path, depth + 1))

    return "Reach limit"


depth_first_limit_o ("S", "G", 2)
# graph_states = {"S": ["C", "B","A"], "A":["D","E"] ,"B":["G"] ,"C":["F"], "D": ["H"], "E": ["G"], "G": ["F"] , "F": [] , "H" : []}

def depth_first_iteration(initial_state):
    frontier = list()
    frontier.append(initial_state)
    iteration_limit =0
    while frontier:
            iteration_limit+=1
            pre = frontier.pop(-1)
            while iteration_limit > 0:
               status = depth_first_limit(pre, iteration_limit)
               if status == "Reach limit":
                   iteration_limit+=1
               else :
                   return status


    return "Not find"

print(depth_first_iteration("S"))