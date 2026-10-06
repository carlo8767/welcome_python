import numpy as np
import scipy.linalg as la

# RETURN AN ARRAY
X = np.loadtxt('train.csv')
y = np.loadtxt('train.label')


# k, X DATA TRAIN , LABEL
def xval(k, X, y):
    '''return the k train/validation splits'''
    # RETURN THE DIMENSION OF THE LABEL
    if len(y.shape) == 1:
        y = y.reshape([-1, 1])
    # IT WILL TELL ME THE SIZE

    blocksize = X.shape[0] // k
    # ROW COLUMS
    print(X.shape)
    print(f'the size is  {blocksize}')
    Xblocks = list()
    yblocks = list()

    for i in range(k - 1):
        # -3.631220589461406689e+00 2.457266113427576393e-01
        Xblocks.append(X[i * blocksize:(i + 1) * blocksize, :])
        yblocks.append(y[i * blocksize:(i + 1) * blocksize, :])

    # handle the last block separately
    Xblocks.append(X[(k - 1) * blocksize:, :])
    yblocks.append(y[(k - 1) * blocksize:, :])

    for x, y in zip(Xblocks, yblocks):
        print(x.shape, y.shape)

    # the output
    Xtrain = list()
    ytrain = list()

    Xval = list()
    yval = list()

    for i in range(k):
        # select the blocks to go into training
        Xtraini = Xblocks[0:i] + Xblocks[i + 1:k]
        ytraini = yblocks[0:i] + yblocks[i + 1:k]

        # prepare a consecutive numpy object
        Xt = np.vstack(Xtraini)
        yt = np.vstack(ytraini)

        # put into the output list
        Xtrain.append(Xt)
        ytrain.append(yt)

        # select the validation blocks for output
        Xval.append(Xblocks[i].copy())
        yval.append(yblocks[i].copy())

    for x, y in zip(Xblocks, yblocks):
        print(x.shape, y.shape)

    return Xtrain, ytrain, Xval, yval


# call xval to give me k=3 splits
xt, yt, xv, yv = xval(3, X, y)


# perceptron training and prediction algorithms
def perceptron_predict(x, w):
    # predict the class of x, given the weight vector w
    # MATRIX MULTIPLICATION ?
    sgn = np.sign(x @ w)
    # numpys sign may return 0. we don't want that
    if sgn != 0:
        return sgn
    else:
        return 1


def perceptron_train(X, y, w=None):
    # initialize w to zero, if it is not given
    if w is None:
        w = np.zeros([X.shape[1]])

    for i in range(X.shape[0]):
        x = X[i, :]
        pred = perceptron_predict(x, w)
        truy = y[i]
        if pred != truy:
            w += truy * X[i, :]

    return w


# simple linear classifier training (prediction can be done with perceptron_predict())
def simple_train(X, y):
    w = la.inv(X.T @ X) @ X.T @ y
    return w


def accuracy(y, pred):
    return (y.flatten() == pred.flatten()).sum() / len(y.flatten())


# cross validation using the perceptron algorithm
accuracies = list()
for xtrain, ytrain, xvali, yvali in zip(xt, yt, xv, yv):
    xtrain = np.hstack([xtrain, np.ones([xtrain.shape[0], 1])])
    w_perceptron = perceptron_train(xtrain, ytrain)

    xvali = np.hstack([xvali, np.ones([xvali.shape[0], 1])])
    prediction = np.array([perceptron_predict(x, w_perceptron) for x in xvali])
    acc = accuracy(yvali, prediction)

    print(f'validation accuracy: {acc}')
    accuracies.append(acc)

print(f'Average validation accuracy for perceptron training is {np.mean(accuracies)} +- {np.std(accuracies)}')

# cross validation using the simple linear classifier
accuracies = list()
for xtrain, ytrain, xvali, yvali in zip(xt, yt, xv, yv):
    xtrain = np.hstack([xtrain, np.ones([xtrain.shape[0], 1])])
    w_simple = simple_train(xtrain, ytrain)

    xvali = np.hstack([xvali, np.ones([xvali.shape[0], 1])])
    prediction = np.array([perceptron_predict(x, w_simple) for x in xvali])
    acc = accuracy(yvali, prediction)

    print(f'validation accuracy: {acc}')
    accuracies.append(acc)

print(f'Average validation accuracy for perceptron training is {np.mean(accuracies)} +- {np.std(accuracies)}')


if __name__ == '__main__':
  arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

  print(arr.shape)
  arr =  np.array([[1, 2, 3]])
  print(arr.shape)
  print(2e-03)
  n = str(3.631220589461406689e00)
  p = str(2.457266113427576393e-01)
  print(len(n)+len(p))
