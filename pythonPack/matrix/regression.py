import numpy as np
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from scipy import stats

class regression:


    def spearman(self):
        list_x = [1, 7, 3, 4, 6, 2,5,8]
        list_y = [79, 47, 86, 69, 71,96,77,50]
        res = stats.spearmanr(list_x, list_y)
        print(f'This is the "spearman correlation {res.statistic}')


    def pearson_correlation(self):

        list_x = [1,2,3,4,5]
        list_y = [1,4,9,16,25]
        pearson_correlation = pearsonr(list_x, list_y)

        # statistic is the pearson correlation
        print(f'This is the "pearson_correlation {pearson_correlation}')

        list_x = [1, 2, 3, 4, 5]
        list_y = [3, 4, 5, 8, 11]
        pearson_correlation = pearsonr(list_x, list_y)

        print(f'This is the "pearson_correlation {pearson_correlation}')




    def data_set (self):
        # PROVIDE DATA SET https://realpython.com/linear-regression-in-python/#simple-linear-regression-with-scikit-learn
        list_x = [1, 1, 1, 1, 1]
        list_y = [3, 0, 0, 1, 4]
        x = np.array(list_x).reshape((-1,1))
        y = np.array(list_y)
        model = LinearRegression()
        # FINDING THE BEST LINEAR MODEL

        model.fit(x,y)
        model.score(x,y)
        # PRINT THE LINEAR MODEL
        print(f"intercept b : {model.intercept_}")
        print(f"slope mx {model.coef_}")
        #Lille Auxerre Under 3.5
        # Empoli vs Venez over 1.5 TAKE IT
        # Augsta vs Eintracth Under 3.5

    def second_data_set(self):
        # PROVIDE DATA SET https://realpython.com/linear-regression-in-python/#simple-linear-regression-with-scikit-learn
        list_x = [2, 2, 2, 2, 2]
        list_y = [4, 2, 4, 4, 2]
        x = np.array(list_x).reshape((-1, 1))
        y = np.array(list_y)
        model = LinearRegression()
        # FINDING THE BEST LINEAR MODEL

        model.fit(x, y)
        model.score(x, y)
        # PRINT THE LINEAR MODEL
        print(f"intercept b : {model.intercept_}")
        print(f"slope mx {model.coef_}")


if __name__ == '__main__':
    test = regression();
    test.data_set()
    test.second_data_set()