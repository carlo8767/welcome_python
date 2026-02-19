from sympy import false


class Test_Depth_Limit:
    class Test_Depth_Limit:

        def __init__(self):
            pass

        def verifyPath(self, graph, destination, currentpath, root):
            for s in graph:
                root += s
                currentpath.append(root)

        def test_breadth_first_search(self):
            # from source to destination f
            graph = {"a": ["b", "c", "d"], "b": ["e"], "c": ["e"], "d": ["e"], "e": ["f"]}
            node_dest = "f"
            visited_nodes = list()
            visited_nodes.append("a")
            list_nodes = list(graph)
            find = True
            ts = self.visited_node(list_nodes.pop(0), graph, visited_nodes, node_dest, find)
            while find:
                self.visited_node(visited_nodes[0][-1], graph, visited_nodes, node_dest, find)

        def visited_node(self, list_nodes, graph, visited_nodes, node_dest, find):
            # Visited nodes
            s = graph[list_nodes]
            # POP THE QUEEU FIFO AND APPEND THE COMBINATION OF THE NODES
            previous_nodes = visited_nodes.pop(0)
            for t in s:
                visited_nodes.append(previous_nodes + t)
                if t == node_dest:
                    find = False
                    print(previous_nodes + t)
                    return find
            return visited_nodes

    if __name__ == '__main__':
        f = Test_Depth_Limit()
        f.test_breadth_first_search()

    def test_preparation_exam (self):
       # from source to destination f
       my_graph = {"a": ["b", "c", "d"], "b": ["e"], "c": ["e"], "d": ["e"], "e": ["f"]}
       source = "a"
       destination = "b"
       # DEPTH SEARCH
















    def find_size_state(self, states):
        n = len(states)
        return (n * (n - 1)) / 2

    def generate_level(self, states):
        # The IDEA THAT I TRY TO SORT ONE BY ONE !!
        # state = [3, 2, 1]
        size = len(states)-1
        set_combination = set()
        array_new = states.copy()
        set_combination.add(tuple(array_new.copy()))
        for i in range(0,size):
            for s in range(i+1, size+1):
                previuos = states[i]
                next = states[s]
                array_new[i] = next
                array_new[s] = previuos
                set_combination.add(tuple(array_new.copy()))
                array_new.clear()
                array_new = states.copy()
        return list(set_combination)



    def explore_path_layer(self, dictionary_list, level):
        # explore layer
        state = dictionary_list[level]
        size = len(state) - 1
        set_combination = set()
        array_new = state.copy()
        set_combination.add(tuple(array_new.copy()))
        for i in range(0, size):
            for s in range(i + 1, size + 1):
                previuos = state[i]
                next = state[s]
                array_new[i] = next
                array_new[s] = previuos
                set_combination.add(tuple(array_new.copy()))
                array_new.clear()
                array_new = state.copy()
        dictionary_list[level + 1] = list(set_combination)


    def explore_path_layer_bomb(self, dictionary_list, limit, level_height, goal):
        # explore layer
        state_dictionary = dictionary_list

        set_combination = list()
        tuple_store = list(state_dictionary["00"])
        size = len(tuple_store)-1
        set_combination.append(tuple_store)
        ts = self.recursive_dynamic(size,set_combination, goal,tuple_store, state_dictionary, "03", level_height)
        return  ts

    def recursive_dynamic(self, size,set_combination, goal ,array_new, state_dictionary, limit_depth, level_height):
        smart_key = 0
        find = False
        length = size
        # WHEN I I INCREASE I I CHANGE THE FLOOR
        for i in range(0, size):
            while length > 0:
                previuos = array_new[i]
                next = array_new[length]
                array_new[i] = next
                array_new[length] = previuos
                # STOR DICTIONARY
                smart_key = str(i)+str(length)
                state_dictionary[smart_key] = tuple(array_new.copy())
                if goal in state_dictionary[smart_key]:
                    return  state_dictionary
                # IF MY STATUS BUT I KEEP EXPLORE REMOVE THE NODES EXPLORED
                elif smart_key == limit_depth:
                    return state_dictionary
                else:
                    array_new[i] = previuos
                    array_new[length] = next
                    ver = state_dictionary.pop(smart_key)
                length -= 1



            length = size
            array_new.clear()
            # the las two
            previuos = array_new[size]
            next = array_new[length-1]
            array_new[i] = next
            array_new[length] = previuos
            combine = str(i)+ str(length+1)
            state_dictionary[combine] = tuple(array_new.copy())
            if goal in state_dictionary[smart_key]:
                return state_dictionary
            array_new = state_dictionary[smart_key]
            state_dictionary.pop(smart_key)

    def test_verify_solution_bomb(self):



        # I CAN USE THIS STRUCTURE LEVEL + WIDTH
        fs = {(00):(3, 2, 1), (11):(2, 3, 1), (12):(2,33,3)}
        # EVERY ITERATIONS I INCREASE OR DECREASE THE WIDHT 21 NOT PRESENT EXTRACT 11 AND GENERATE COMBINATIONS
        ns = fs.pop(12)
        goal_states = (1,3,2)
        states = {"00":(3, 2, 1)}
        ns = self.explore_path_layer_bomb(states, 1,1, goal_states)
        print(ns)





    def test_verify_solution_explore(self):
        states= [3, 2, 1]
        dictionary_states = {0:states}
        limit_height = 0
        limit_vertical =0
        self.explore_path_layer(dictionary_states, 0)
        ps = dictionary_states.pop(0)
        rm = dictionary_states.pop(1)
        for ns in enumerate(rm):
           p = rm.pop(ns)
        print(rm)




    def test_generate_possible_combination(self):
        state = [3, 2, 1]
        goal_state = [(3, 1, 2)]
        path_reach_destination = list()
        find_path = False
        while not find_path:
            array_search = state
            state_path = self.generate_level(array_search)
            expected = [(3, 2, 1),(2, 3, 1),(1, 2, 3), (3, 1, 2)]
            # VERIFY IF I FIND THE STATE USE A DICTIONARY TO CREATE THE GRAPH LEVEL BY LEVEL
            assert  sorted(state_path) == sorted(expected)


    def test_generate_layer(self):
        state = [3, 2, 1]
        goal_state = [(3, 1, 2)]
        path_reach_destination = list()
        find_path = False
        while not find_path:
            array_search = state
            state_path = self.generate_level(array_search)
            expected = [(3, 2, 1),(2, 3, 1),(1, 2, 3), (3, 1, 2)]
            # VERIFY IF I FIND THE STATE USE A DICTIONARY TO CREATE THE GRAPH LEVEL BY LEVEL
            assert  sorted(state_path) == sorted(expected)




    def test_size(self):
        # states is only three
        state = [3, 2, 1, 4]
        value = self.find_size_state(state)
        assert value == 6


if __name__ == '__main__':

    thisset = {"apple", "banana", "cherry"}

    thisset.add("orange")

    print(thisset)
