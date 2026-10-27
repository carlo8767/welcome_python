import string

import openml
import category_encoders as ce

from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score
from sklearn.calibration import CalibratedClassifierCV



def load_dataset(id_dataset:int, target_label:string):
        dataset = openml.datasets.get_dataset(id_dataset)
        X, y, categorical_indicator, attribute_names = dataset.get_data(
            target= target_label
        )

if __name__ == '__main__':

    # Load dataset
    dataset = openml.datasets.get_dataset(31)

    X, y, categorical_indicator, attribute_names = dataset.get_data(
        target=  "class"
    )


    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )


    # Encode categorical features
    categorical_cols = X_train.select_dtypes(
        include=['category']
    ).columns

    encoder = ce.OrdinalEncoder(
        cols=categorical_cols
    )

    X_train = encoder.fit_transform(X_train)
    X_test = encoder.transform(X_test)
    # ORIGINAL
    original = encoder.inverse_transform(X_train)

    # Encode target
    label_encoder = LabelEncoder()

    y_train = label_encoder.fit_transform(y_train)
    y_test = label_encoder.transform(y_test)


    # Create models
    model1 = LogisticRegression(
        random_state=42,
        max_iter=500000
    )

    model2 = DecisionTreeClassifier(
        random_state=42
    )

    model3 = CalibratedClassifierCV(SVC(random_state=42), ensemble=False)


    # Hard Voting Classifier
    hard_voting = VotingClassifier(
        estimators=[
            ('lr', model1),
            ('dt', model2),
            ('svc', model3)
        ],
        voting='hard'
    )


    # Train
    hard_voting.fit(X_train, y_train)



    # Individual predictions
    lr_pred = hard_voting.named_estimators_['lr'].predict(X_test)
    dt_pred = hard_voting.named_estimators_['dt'].predict(X_test)
    svc_pred = hard_voting.named_estimators_['svc'].predict(X_test)


    print(dt_pred.shape)


    # Final voting prediction
    voting_pred = hard_voting.predict(X_test)

    # ORIGINAL CLASS
    originalTwo = label_encoder.inverse_transform(voting_pred)


    # Individual accuracy
    print(
        f"Logistic Regression Accuracy: "
        f"{accuracy_score(y_test, lr_pred):.2f}"
    )



    print(
        f"Decision Tree Accuracy: "
        f"{accuracy_score(y_test, dt_pred):.2f}"
    )

    print(
        f"SVC Accuracy: "
        f"{accuracy_score(y_test, svc_pred):.2f}"
    )

    # precision
    print(
        f"Hard Voting Precision: "
        f"{accuracy_score(y_test, voting_pred):.2f}"
    )

    # Individual precision
    print(
        f"Logistic Regression Precision: "
        f"{precision_score(y_test, lr_pred):.2f}"
    )

    print(
        f"Decision Tree Precision: "
        f"{precision_score(y_test, dt_pred):.2f}"
    )

    print(
        f"SVC Precision: "
        f"{precision_score(y_test, svc_pred):.2f}"
    )

    print(
        f"Hard Voting Precision: "
        f"{precision_score(y_test, voting_pred):.2f}"
    )


    # recall

    print(
        f"Logistic Regression recall: "
        f"{recall_score(y_test, lr_pred):.2f}"
    )

    print(
        f"Decision Tree recall: "
        f"{recall_score(y_test, dt_pred):.2f}"
    )

    print(
        f"SVC recall: "
        f"{recall_score(y_test, svc_pred):.2f}"
    )

    print(
        f"Hard Voting recall: "
        f"{recall_score(y_test, voting_pred):.2f}"
    )

    aggregate = (recall_score(y_test, voting_pred)+precision_score(y_test, voting_pred))/2

    print(f'aggregation score modelOne {aggregate}')

    # https://www.kaggle.com/code/pythonafroz/votingclassifier-a-powerful-ensemble-technique