from math import sqrt

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

def euclidian_distance(training_set):
    elements = [x for x in training_set.tolist()]
    list_distance = list()
    for i in range(0, len(elements)-1):
        x1, y1, z1 = elements[i]
        x2, y2, z2 = elements[i+1]
        distance = ((x2-x1)**2) +((y2-y1)**2) + ((z2-z1)**2)
        squareit = sqrt(distance)
        list_distance.append((i,i+1, squareit))
    print(list_distance)

def euclidian_distance_from_k(training_set, k, training_label)->list :
    elements = [x for x in training_set.tolist()]
    list_distance = list()
    x2, y2, z2 = k
    for i in range(0, len(elements)):
        if k == elements[i]:
            continue
        else :
            x1, y1, z1 = elements[i]
            distance = sqrt(((x2-x1)**2) +((y2-y1)**2) + ((z2-z1)**2))
            list_distance.append((k, i, distance, training_label[i]))
    return list_distance

def knn_classifier(training_set, training_label):
    number_k = 19
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0

    threshold = 7+9+31
    to_list = training_set.tolist()
    for k in range (0, len(to_list)):
         t,r,e = to_list[k]
         if (t+r+e)<threshold:
             a = euclidian_distance_from_k(training_set, to_list[k] , training_label)
             a.sort(key=lambda  x : x[2])
             pred_1 = sum(1 for i in range(number_k) if a[i][3] == 1)
             pred_not1 = sum(1 for i in range(number_k) if a[i][3] == -1)
             #  predict one
             if  pred_1 > pred_not1:
                 if training_label[k] == 1:
                     true_positive += 1
                 else :
                      false_positive+=1
             else :
                 if training_label[k] == -1:
                     true_negative += 1
                 else:
                      false_negative+= 1


    accuracy = ((true_positive+true_negative)/ (true_negative+false_positive+false_negative+true_positive))
    precision = ((true_positive)/ (true_positive+false_positive))
    recall  = ((true_positive)/ (true_positive+false_negative))
    print(f'the accuracy is {accuracy}, precision is  {precision} and recall is  {recall}')







# loading traning set and respective labels from files
# NOTE: only works if they are in the same folder as the Python file!
training_set = read_dataset("training_set")
print(type(training_set))
# CHECK SHAPE 360 entity with 3 columns each
a = training_set.shape
training_labels = read_labels("training_labels")
knn_classifier(training_set, training_labels)

# loading validation set and respective labels from files
# NOTE: only works if they are in the same folder as the Python file!
validation_set = read_dataset("validation_set")
validation_labels = read_labels("validation_labels")

