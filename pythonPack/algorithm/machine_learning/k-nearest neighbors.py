import numpy as np

# simple function to read the datasets
def read_dataset(file_name):
    f = open(file_name, "r")
    points = []
    for i in f.readlines():
        x, y, z = i.split(sep=",")
        points += [np.array([float(x),float(y),float(z)])]
    f.close()
    return np.array(points)

# simple function to read the labels assigned to points in the datasets
def read_labels(file_name):
    f = open(file_name, "r")
    labels = []
    for i in f.readlines():
        values = i.split()
        labels += [int(values[0])]
    f.close()
    return np.array(labels)

# loading traning set and respective labels from files
# NOTE: only works if they are in the same folder as the Python file!
training_set = read_dataset("training_set")
training_labels = read_labels("training_labels")

# loading validation set and respective labels from files
# NOTE: only works if they are in the same folder as the Python file!
validation_set = read_dataset("validation_set")
validation_labels = read_labels("validation_labels")


# have fun implementing the KNN classifier!

def euclidian_distance():
   array_dimension = np.array([[3, 3, 3], [0, 1, 2]])

   list_euclidian_distance = list()
   size_array = len(array_dimension)
   count_columns = 0
   euclidian_distances = 0
   for v, n in enumerate(array_dimension):
       count_columns+=1
       if count_columns >= size_array:
           break
       for t,s in enumerate(n):
          distance = (array_dimension[v+1][t]-s)
          distance = pow(distance, 2)
          list_euclidian_distance.append(distance)
       list_euclidian_distance.append(sum(x for x in list_euclidian_distance))





euclidian_distance()
array_dimension = np.array([[3,3,3],[0,1,2]])
array_dimension.std()
# Get the square of the difference of the 2 vectors
square = np.square(array_dimension[0], array_dimension[1])
# Get the sum of the square
sum_square = np.sum(square)
# Column raw
print(array_dimension[1][0])