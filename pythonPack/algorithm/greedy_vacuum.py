import random



class TestGreedy:



    def test_status_man(self):
        status = [("X"),("X"),("V"),("")]
        goal = [[("ND"),("V"),("ND"),("ND")]]
        cost = self.combinations_heuristic_movement(status,goal)
        heuristic = self.heuristic_cost(status)
        next_cost = 0
        tree_expansion = dict()
        tree_expansion [tuple(status)] = heuristic
        tree_expansion = self.expands_solutions(status, goal, 0, tree_expansion, next_cost, 0)





    def expands_solutions(self, set_status, set_goal, count_set, tree_status, next_cost, original):
        next_cost = 0
        action = ["CLEAN", "ML", "MR"]
        pos_vacuum = set_status.index("V")
        new_status = set_status
        while count_set < 3:
            # NUMBER ACTION
            action_performed = random.choice(action)
            if action_performed == "ML" and  (pos_vacuum-1) > 0:
                new_status[pos_vacuum-1]+= "V"
                new_status[pos_vacuum].replace("V", "")
                next_cost+=1
            elif action_performed == "MR" and (pos_vacuum+1) < len(set_status):
                new_status[pos_vacuum +1] += "V"
                new_status[pos_vacuum].replace("V", "")
                next_cost += 1
            elif action_performed == "CLEAN":
                new_status[pos_vacuum].replace("X", "")
                next_cost += 2
            if tuple(new_status) not in tree_status:
                heuristich_cost = self.heuristic_cost(set_status)
                tree_status[tuple(new_status.copy)] = next_cost+heuristich_cost
                next_cost = 0
            else:
                self.expands_solutions(set_status, set_goal, count_set, tree_status, next_cost, original)
            # MEMORY THE COST

            next_cost = 0
            return  self.expands_solutions(set_status, set_goal, count_set+1, tree_status, next_cost, original)

        return tree_status





    def heuristic_cost(self, status):
        count =0
        for n in status:
            if "X" in n:
                count+=1
        return  count *2






    def combinations_heuristic_movement(self, status, desirable_status):
        new_status = status.copy()
        cost_movement = 0
        cost_clean = 1
        key_dirty = [x for x in status if "X" in x]
        for n in key_dirty:
            key_vacuum = [x for x in new_status if "V" in x]
            pos_vacuum = new_status.index(key_vacuum[0])
            pos_dirty = new_status.index(n)
            cost_movement += abs(pos_dirty - pos_vacuum)
            new_status[pos_dirty] = "V"
            new_status[pos_vacuum] = ""
            cost_clean *=  2
        return cost_movement + cost_clean







    def test_vacuum(self):
        ns = [("..."),("..."), ("C"),("D")]
        set_status = [("A"), ("B")]
        dictionary_status = dict()
        count = self.possible_combinations(set_status)
        self.create_combination(count,set_status, dictionary_status)
        combination_vacuum = count * 2


    def create_combination(self, count, status, dictionary_combinations):
        list_status = list()
        set_status = [("A"), ("BX"), ("CX"), ("DX")]
        a = ["", "X"]
        # b = ["NV", "V"]
        if count == 0:
            # RETURN THE VARIOUS COMBNINATION X IS DIRTY
            return dictionary_combinations
        for i in range(0, len(status)-1):
            rand_external = random.choice(a)
            # vacuuum = random.choice(b)
            external = status[i] + rand_external
            list_status.append(external)
            for n in range((i+1), len(status)):
                rand_internal = random.choice(a)
                ts = status[n]+rand_internal
                list_status.append(ts)
            if list_status in dictionary_combinations.values():
                return self.create_combination(count, status, dictionary_combinations)
            dictionary_combinations[count] = list_status
            count -= 1
            return  self.create_combination(count, status, dictionary_combinations)




    def test_greedy(self):
        set_status = [("A"),("B"), ("C"),("D")]
        combine = self.create_combination_dirty_no_dirty(set_status)
        list_verify = ["AD","AND", "BD", "BND", "CD", "CND", "DD","DND"]
        assert combine == list_verify
        value = self.heuristich_possible_combinations(set_status)
        assert value == 64
        set_status = [("A"),("B"), ("C"),("D")] * 2
        print(set_status)


    def create_combination_dirty_no_dirty(self, status):
        dirty = "D"
        no_dirty = "ND"
        list_status = list(status)
        dictionary_combinations = dict()
        list_combination_status = list()
        for i in list_status:
            combine_dirty = i+dirty
            combine_no_dirty = i + no_dirty
            list_combination_status.append(combine_dirty)
            list_combination_status.append(combine_no_dirty)
        return  list_combination_status

    def possible_combinations (self, status):
            return len(status)* len(status)

    def heuristich_possible_combinations(self, status):
        return (len(status)* len(status))*4

    def heuristich_combinations_chane(self, status, goal):
        pass




