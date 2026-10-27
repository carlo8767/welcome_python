import openml
import sklearn.ensemble
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
# 1. Fetch the flow by its ID (e.g., flow ID 8317)
flow_one = openml.flows.get_flow(126561)

# 2. Reconstruct the untrained model architecture/pipeline
# model = openml.flows.flow_to_model(flow)
model = flow_one.extension.flow_to_model(flow_one)

# The 'model' variable is now a standard, trainable scikit-learn object!
# https://docs.openml.org/python/extensions/
# https://openml.github.io/openml-python/latest/
# AFTER I JUST PASS THE DATABASE https://docs.openml.org/reference/flows/ --> RUN A TASK AND EVALUATE THE MODEL
# OR I CAN PASS A BENCHMARK DATASET AND EVALAUTE PRECISE TASK
# pip uninstall -y $(pip list | grep -E "nvidia|cuda" | awk '{print $1}')


# Build any model you like
clf = ensemble.RandomForestClassifier()

# Download any OpenML task
task = tasks.get_task(3954)

# Run and evaluate your model on the task
run = runs.run_model_on_task(clf, task)




dataset = openml.datasets.get_dataset(31)
# target specify what is your label
X, y, _, _ = dataset.get_data(target="existing_credits")




