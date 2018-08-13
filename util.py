import os
import run_nn
import run_dt
import run_rf

AVAILABLE_ALGORITHMS = {'DT': run_dt, 'RF': run_rf, 'NN': run_nn}
REPEAT_ITERATION = {'DT': 100, 'RF': 100, 'NN': 100}
ALGORITHMS_NUMS = {'DT': 0, 'RF': 1, 'NN': 2}
ALGORITHMS_NAMES = {'DT': 'Decision Tree', 'RF': 'Random Forest', 'NN': 'Nearest Neighbors'}
FEATURES_MODULES_NUMBER = 3
AUTHORS_NUM = len(os.listdir("corpus/data"))
TEST_SIZE = 0.2
