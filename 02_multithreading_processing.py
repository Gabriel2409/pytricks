
# https://towardsdatascience.com/understanding-python-multithreading-and-multiprocessing-via-simulation-3f600dbbfe31
""" A simple code to demonstrate multi threading/processing efficiencies over IO/CPU-heavy tasks
    Author: Pan Wu (https://github.com/PanWu)
    1. ensure all required packages are installed (under Python 3 environment)
    2. run "python code.py", and wait to see the result print out
"""

import time
import timeit
import random
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

def io_heavy_function(dummy_input: int):
    ''' mimic IO heavy task (e.g. download webpage) using time.sleep
    '''
    tot = random.randint(0, 10000)
    time.sleep(0.1)
    return tot % 10

def cpu_heavy_function(dummy_input: int):
    ''' mimic CPU heavy task (e.g. scientific calculation) using random.randint
    '''
    tot = sum([random.randint(0, 10) for i in range(110000)])
    return tot % 10

def eval_parallel(parallel_method: str, function_type: str, n_workers: int):
    ''' evaluate multi-thread or multi-process performance '''
    # whether use multi thread or multi process
    parallel_method_dict = {
        'multithread': ThreadPoolExecutor,
        'multiprocess': ProcessPoolExecutor
    }
    # whether the function is io-heavy or cpu-heavy
    function_type_dict = {
        'io_heavy': io_heavy_function,
        'cpu_heavy': cpu_heavy_function
    }
    the_method = parallel_method_dict[parallel_method]
    the_function = function_type_dict[function_type]

    # run the function for 100 times (~10 seconds), and use n_workers to parallel
    n_item = 100
    with the_method(n_workers) as executor:
        results = executor.map(the_function, range(n_item))
    return sum([x for x in results])


if __name__ == "__main__":

    # initiate with all the parallel computing method and function types
    method_function_list = [
        ("multithread", "io_heavy"),
        ("multithread", "cpu_heavy"),
        ("multiprocess", "io_heavy"),
        ("multiprocess", "cpu_heavy")]

    # how many times the eval_parallel is calculatd to provide an accurate measure
    n_eval = 5
    n_worker_list = range(1, 9)
    result_df_list = []

    # run the given parallel methods & functions sequentially
    for the_method, the_function in method_function_list:
        time_list = [timeit.timeit(
            'eval_parallel("{0}", "{1}", {2})'.format(the_method, the_function, n_worker),
            number=n_eval, globals=globals()) / n_eval for n_worker in n_worker_list]
        print(' -- completed evalulate: {0}, {1} -- '.format(the_method, the_function))
        result_df_list.append(pd.DataFrame({
            'method': the_method,
            'function': the_function,
            'n_workers': n_worker_list,
            'time_spent': time_list}))
    result_df = pd.concat(result_df_list)
    print(result_df)


"""
Multithreading and Multiprocessing are equally effective in IO heavy tasks. With more workers, the time spent over the total tasks decreases from ~ 10 seconds (1 worker) to 1.3 seconds (8 workers), which represents around 8X speed-boosting.
Multithreading does not work well on CPU heavy tasks. The red bar chart shows regardless of how many threads are used, the total time spent is constantly around 10 seconds.
Multiprocessing is effective over CPU heavy tasks, however, it reaches a plateau under hardware limits. In my case, it is when worker # is ≥ 5, its maximum speed-boosting is still 5X (~2 seconds), less than their actual worker # (e.g. 6, 7, 8). This is because my laptop has 6 cores, and given the system requires 1 core to maintain its functions, the rest 5 cores can be used for computing, hence maximum speed boosting is 5X.

"""

# https://realpython.com/python-gil/