import numpy as np
from itertools import product
class DataLoader:


 def __init__(self):
    self.input_neuron = np.zeros([4,2])


 def cartesian_product (self, matrix_values):
     # CARTESIAN PRODUCT
     return list(product(*matrix_values))


 def add_elements_to_np_array(self, np_array):
    print
    for x,y in enumerate(np_array):
        # add the raw to the matrix
        self.input_neuron[x] = y









if __name__ == '__main__':
        # m = np.zeros([16,4])
        # data_loader = DataLoader()
        # list_iterator = data_loader.cartesian_product(([0,1],[1,1]))
        # data_loader.add_elements_to_np_array(list_iterator)
        # print(data_loader.input_neuron)
        # print(list_iterator)
        # random_input = np.random.randint(0,4)
        # print(random_input)
        # ts = data_loader.input_neuron[random_input]
        # print(data_loader.input_neuron)
        # print("random raw")
        #
        # print(data_loader.input_neuron[1])
        #
        # create an np array 5 raw and 3 columns
        matrix = np.zeros((32, 3))
        # add at array some values
        values = [0,1],[0,1],[0,1],[0,1]
        result = np.array(list((product(*values))))
        print(result.shape)
        print(result[1:3])

        print(result)
        # SLICING
        matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print("separate")
        print(matrix[1:3])
        afa = np.array([10, 20, 30, 40, 50])
        print(afa.shape)

        arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

        print(arr[1:2])