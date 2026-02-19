from prompt_toolkit.key_binding.bindings.named_commands import previous_history

from pythonPack.algorithm.recursion import length


class TestIterative:


     def test_combinations(self):

         dg = [1,2,4]
         st = (1,2,4)
         ms = list(st).pop()
         root = [(1,2,3)]
         # LIMIT IS INCREASE BASE ON THE MAXIMUN COMBINATIONS
         limit_permutations = 2 *len(root[0])
         # LIMIT IS THE MAXIMUN DEPTH ITERATIVE
         # COUNT IS THE NUMBER OF LAYER YOU HAVE TO EXPLORE
         tree_nodes = {0:list()}

         all_comb = self.generate_combination(root, limit_permutations, 0, tree_nodes)


         roots = [(1,2,3),(2,1,3),(3,2,1),(1,3,2)]
         sorted(all_comb) == sorted(roots)



     def generate_combination(self, combo,limit_permutations, count,tree_nodes):
         size = len(combo[count])
         if count == limit_permutations-1:
             return combo
         for ext in range(0,size-1):
             # EXPLORE THE LAYER
             store_arr = list(combo[count])
             for i in range(ext+1, size):
                 previous = store_arr[ext]
                 next = store_arr[i]
                 store_arr[ext] = next
                 store_arr[i] = previous
                 if tuple(store_arr) in combo:
                     continue
                 else :
                     combo.append(tuple(store_arr.copy()))
                     if count  in tree_nodes.keys():
                        tree_nodes[count].append(tuple(store_arr.copy()))
                     else:
                         tree_nodes[(count)]= list()
                         tree_nodes[count].append(tuple(store_arr.copy()))
                     store_arr.clear()
                     store_arr = list(combo[count])

         return  self.generate_combination(combo, limit_permutations, count+1, tree_nodes)








