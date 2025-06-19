"""
The exercise was demanding and required me to evaluate different perspectives to find the correct approach. The code uses the Dijkstra algorithm to find the shortest path with the lowest weight combined with a priority queue.
Firstly, Object TableCostNodes contains the initial probability of success, for the various nodes. It assigns a value of one for the first nodes and for the other nodes an infinity probability.
Secondly, NodesEdge, stores the nodes, their edges, and the single probability of success in reaching the target. Successively, every Node it saved in a dictionary that keeps the nodes in numerical order, and it creates the association nodes, with multiple edges.
Thirdly, the method dijkstra_priority_creation uses a priority queue, that allows to pop element to always with the lowest values. This ensures, that I evaluate the nodes in order of lower priority to fail.
Finally, I have the variable's success that is pushed with the compound success rates and the nodes.
At the end, I can extract from the last node, the compound probability with the highest rates of success.

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

DIJISTRKA ALGORITHM REQUIRED:
1. Create a list of nodes that have the cost to reach the node ( the starting point the cost should be 0), the cost , and the previous node
2. Create a queue where you store the edge with its cost
3. Extract with pop the lowest probability ( the beginning is 0). Pop remove
4  add the cost + the next cost edge
5. Store the previous node
6. When you reach the end you will find the shortest past and its cost
"""

import heapq


class TableCostNodes:
    def __init__(self, node, cost_move, next_node):
        self.node = node
        self.cost_move = cost_move
        self.next_node = next_node


class NodesEdge:
    def __init__(self, node, probability_success, next_edge):
        self.node = node
        self.probability_success = probability_success
        self.next_edge = next_edge


def create_table_track(limit) -> dict:
    list_table_prior = dict()
    index = 1
    while index <= limit:
        if index == 1:
            ts = TableCostNodes(index, 1, None)
            list_table_prior[index] = ts
            index += 1
        else:
            ts = TableCostNodes(index, float("inf"), None)
            list_table_prior[index] = ts
            index += 1
    return list_table_prior


def dijkstra_priority_creation(list_nodes_edge, table_nodes_track):
    queue = list()
    priority_queue = heapq
    # COST NODES
    priority_queue.heappush(
        queue, (-1, 1)
    )  # THE FIRST IS THE PROBABILITY TO NOT FALL DOWN THE SECOND THE NODE
    # VISITED THE EDGE WITH LOWEST PRIORITY
    while queue:
        prob, current_node = heapq.heappop(queue)
        if prob > table_nodes_track[current_node].cost_move:
            continue
        for lne in list_nodes_edge[current_node]:
            # VISITED THE EDGE AND PUSH
            # CALCULATE COST TAKE IN ACCOUNT THE START
            if prob < 0:
                # KEEP NEGATIVE
                success_rate = prob * lne.probability_success  # EXTRACT THE PROBABILITY
            else:
                success_rate = (
                    prob * -1
                ) * lne.probability_success  # EXTRACT THE PROBABILITY

            # ADD THE NEXT POINTER
            priority_queue.heappush(queue, (success_rate, lne.next_edge))
            # UPDATE TABLE TRACK
            objects = table_nodes_track[lne.next_edge]
            if success_rate < objects.cost_move:
                objects.cost_move = success_rate

    success = table_nodes_track[len(table_nodes_track)]
    print(f"{success.cost_move*-1:.6f}")


def verify_constraint_number(n):
    verify = True
    if n < 2:
        verify = False
    elif n > 10000:
        verify = False
    return verify


def recover_input():

    number_lilies, possible_jumps = input().split()
    convert_number = int(number_lilies)
    convert_jump = int(possible_jumps)
    if verify_constraint_number(convert_number):
        list_nodes_edge = {i: [] for i in range(1, convert_number + 1)}
        nodes_track = create_table_track(convert_number)

        # CREATE DICTIONARY
        while convert_jump > 0:
            nodes, edge, prob_fall_down = input().split()
            convert_nodes = int(nodes)
            next_converts_edge = int(edge)
            if convert_nodes < next_converts_edge:
                # CREATE OBJECT NODES WITH IT OWN EDGE
                probability_fall_down_conversion = float(prob_fall_down)
                probability_of_success = 1 - probability_fall_down_conversion
                edge_prob = NodesEdge(
                    convert_nodes, probability_of_success, next_converts_edge
                )
                # EXTRACT THE OBJECT AND STORE THE CORRECT ORDER
                list_nodes_edge[convert_nodes].append(edge_prob)
                convert_jump -= 1
            else:
                convert_jump -= 1
        dijkstra_priority_creation(list_nodes_edge, nodes_track)


if __name__ == "__main__":

    list_number = [1,2,3,0]
    heapq.heapify(list_number)
    print (heapq.heappop(list_number))
    # I CREATE SOME ELEMENT WIT THE PRIORITY AND THE TYPE
    number = list()
    heapq.heappush(number, (0,"Green"))
    heapq.heappush(number, (1, "Orange"))
    heapq.heappush(number, (2, "Yellow"))
    heapq.heappush(number, (3, "Red"))
    # PRINT THE LARGEST
    print(heapq.nlargest(1, number))
    print(heapq.heappop(number))
    print(heapq.heappop(number))
