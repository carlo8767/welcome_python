
import workshopOne as w1

class Test_workshop_week_one:
# itertools possible integration


        def test_bin_cart (self):
            set_a = {"x","a"}
            set_b = {'b'}
            cartesian_product = w1.bin_cart(set_a, set_b)
            cartesian_result = {('a', 'b'), ('x', 'b')}
            assert cartesian_product == cartesian_result

        def test_binary_concat (self):

            set_a = {'a'}
            set_b = {'a', 'b'}
            set_tuple_a = {('a', 'b', 'a'), ('a', 'b')}
            set_tuple_b = {('a',), ('a', 'a')}
            cartesian_product = {('a','a'), ('a' ,'b')}
            assert w1.bin_cart(set_a, set_b) == cartesian_product
            tuple_verify_variation = {('a' 'a', 'a'), ('a', 'b', 'a', 'a', 'a')}
            result = w1.bin_concat_variation(set_a, set_b)
            assert result == tuple_verify_variation
            set_tuple_a = {('a', 'b', 'a'), ('a', 'b')}
            set_tuple_b = {('a',), ('a', 'a')}
            tuple_verify_concatenation = {('a', 'b', 'a', 'a'), ('a', 'b', 'a', 'a', 'a'), ('a', 'b', 'a')}
            binary_concatenation = set()
            for n in set_tuple_a:

                for x in set_tuple_b:
                    binary_concatenation.add(n+x)

            assert  binary_concatenation == tuple_verify_concatenation

        def test_bin_cart_non_binary(self):
            binary_concatenation = set()
            list_n_tuple = [{('1',), ('2',), ('3','4')}, {('9',), ('8',)}]
            for a in range(1):
                s = list_n_tuple[a]
                for nn in s:
                    for b in range(1, len(list_n_tuple)):
                        for n in list_n_tuple[b]:
                            binary_concatenation.add(nn+n)
            result = {('3', '4', '8'), ('2', '9'), ('1', '9'), ('3', '4', '9'), ('2', '8'), ('1', '8')}
            assert  result == binary_concatenation

        @staticmethod
        def myfunc():
            values = 1, 2, 3
            return list(values)


        @staticmethod
        def tuple():
            return {(8,0), (1,4)}

        def test_lambda(self):
            # Lambda is  faster than loop
            hello_lambda = lambda x: x + 5
            value = hello_lambda(10)
            assert value == 15
            # MAP THE RESULT OF FUNCTION AS PARAMETER
            """
            map() function in Python applies a given function to each element of 
            an iterable (list, tuple, set, etc.) and returns a map object (iterator). 
            It is a higher-order function used for 
            uniform element-wise transformations, enabling concise and efficient code
            """
            result = list(map(lambda x: x+1,self.myfunc()))
            assert result[1] == 3
            result = set(map(lambda x: x[0]+x[1], self.tuple()))
            assert list(result ) [0] == 8

        def test_second_lambda(self):
            result = lambda x: x[0]+x[1]
            list_value = [3,2,1]
            n =  result(list_value)
            assert n == 5









