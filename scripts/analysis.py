import os
import sys
import cPickle
import numpy as np



# PARAMS
log_dir = "/scratch/sforestier001/logs/CogSci2017/2017-01-15_14-13-31-TEST"
config_list = ["RMB"]
n_iter = 10



# RETRIEVE LOGS
trial_list = range(1,n_iter + 1) 
data_vocal_errors = {}

for config_name in config_list:
    data_vocal_errors[config_name] = {}
    for trial in trial_list:
        data_vocal_errors[config_name][trial] = {}
        filename = log_dir + '/pickle/log-{}-{}'.format(config_name, trial) + '.pickle'
        with open(filename, 'r') as f:
            log = cPickle.load(f)
        data_vocal_errors[config_name][trial] = log["environment"]["best_vocal_errors_evolution"]
        

# DUMP RESULT
if not os.path.exists(log_dir + "/results"):
    os.mkdir(log_dir + "/results")
    
filename = log_dir + '/results/vocal.pickle'
with open(filename, 'wb') as f:
    cPickle.dump(log, f)
f.close()
            