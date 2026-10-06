import openml
from sklearn.ensemble import RandomForestClassifier
if __name__ == '__main__':


                openml.config.apikey = ''
                suite = openml.study.get_suite("amlb-classification-all")  # Get a curated list of tasks for classification
                task = openml.tasks.get_task(31)


                #  https://docs.openml.org/examples/20_basic/simple_suites_tutorial/
                suites = openml.study.get_suite(99)
                tasks = suite.tasks
                print(suites)
                print(tasks)
                clf = RandomForestClassifier()
                for task_id in tasks[:3]:
                        task = openml.tasks.get_task(31)
                        run = openml.runs.run_model_on_task(clf, task)
                        score = run.get_metric_fn("predictive_accuracy")
                        print(task.get_dataset().name, score)







