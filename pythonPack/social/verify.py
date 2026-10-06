import openml
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier  # <-- 1. Import RandomForest
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import numpy as np


def evaluate_openml_benchmark(dataset_id: int, model=None, cv: int = 20):
    """
    Evaluate a model on an OpenML dataset using cross-validation.
    """
    # 1. Load dataset from OpenML
    dataset = openml.datasets.get_dataset(dataset_id)
    X, y, categorical_indicator, attribute_names = dataset.get_data(
        target=dataset.default_target_attribute
    )

    # 2. Handle missing model
    if model is None:
        model = LogisticRegression(max_iter=1000)

    # 3. Build a simple pipeline
    pipeline = make_pipeline(
        StandardScaler(with_mean=False),
        model
    )

    # 4. Evaluate using cross-validation
    scores = cross_val_score(
        pipeline,
        X,
        y,
        cv=cv,
        scoring="accuracy"
    )

    # 5. Return benchmark-style results
    return {
        "dataset_id": dataset_id,
        "mean_accuracy": np.mean(scores),
        "std_accuracy": np.std(scores),
        "fold_scores": scores
    }


# ---------------------------
# Example usage
# ---------------------------
if __name__ == "__main__":
    # 2. Instantiate the Random Forest model
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

    # 3. Pass it into your function
    result = evaluate_openml_benchmark(dataset_id=37, model=rf_model)

    print("Benchmark Result (Random Forest):")
    print("Mean Accuracy:", result["mean_accuracy"])
    print("Std Dev:", result["std_accuracy"])
    print("Fold Scores:", result["fold_scores"])