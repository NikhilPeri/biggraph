import os
import gc
import psutil
from time import time
import matplotlib.pyplot as plt

BYTE_TO_MB = float(2**20)

def no_args_func():
    return []

def plot_performance(iterations, func, arg_func=no_args_func):
    execution_time = []
    memory_usage = []
    process = psutil.Process(os.getpid())

    for i in range(iterations):
        gc.disable()
        args = arg_func()
        start_time = time()

        func(*args)

        execution_time.append(time() - start_time)
        memory_usage.append(process.memory_info()[0] / BYTE_TO_MB)
        gc.enable()

    fig, ax1 = plt.subplots()
    ax1.plot(execution_time, 'b.')
    ax1.set_xlabel('Calls to {}'.format(func))
    ax1.set_ylabel('Execution Time (s)', color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.plot(memory_usage,'r.')
    ax2.set_ylabel('Memory Usage (mB)', color='r')
    ax2.tick_params('y', colors='r')

    fig.tight_layout()
    plt.show()

if __name__ == '__main__':
    ITERATIONS=int(1e6)
    import pdb; pdb.set_trace()
    from biggraph.graph import DaskGraph
    import random

    d = DaskGraph()

    def args():
        return [random.randint(0, ITERATIONS), random.randint(0, ITERATIONS), random.random()]

    plot_performance(ITERATIONS, d.add_edge, arg_func=args)

    def args():
        return [random.randint(0, ITERATIONS), random.randint(0, ITERATIONS)]

    plot_performance(ITERATIONS, d.get_edge, arg_func=args)
