import numpy as np
from random import uniform
from math import sqrt
from time import time
from concurrent.futures import ProcessPoolExecutor

e = ProcessPoolExecutor()

# v1
# def throw_dart(i):
#     #number_of_darts_in_circle = 0
#     x, y = uniform(0, 1), uniform(0, 1)
#     if sqrt((x - 0.5)**2 + (y - 0.5)**2) <= 0.5:
#         return 1.0
#     else:
#         return 0.0
    
# if __name__ == '__main__':
#     number_of_darts = 5000
    
#     start_time = time()
#     results = list(e.map(throw_dart, range(number_of_darts)))
#     execution_time = time() - start_time
    
#     number_of_darts_in_circle = np.sum(results)
#     pi_approx = 4*number_of_darts_in_circle/number_of_darts
    
#     print(f"Number of darts: {number_of_darts}")
#     print(f"Pi approximation: {pi_approx}")
#     print(f"Execution_time (s): {execution_time}")
#     print(f"Darts thrown per second: {number_of_darts/execution_time}")
   

# v2
def in_circle(i):
    #number_of_darts_in_circle = 0
    x, y = uniform(0, 1), uniform(0, 1)
    if sqrt((x - 0.5)**2 + (y - 0.5)**2) <= 0.5:
        return 1.0
    else:
        return 0.0

    
def throw_darts(number_of_darts):   
    results = list(e.map(in_circle, range(number_of_darts)))
    number_of_darts_in_circle = np.sum(results)
    pi_approx = 4*number_of_darts_in_circle/number_of_darts
    
    return pi_approx
    
#import matplotlib.pyplot as plt  

if __name__ == '__main__':
    number_of_darts = np.arange(45000, 50000, 1000)
    pi_approxs = []
    execution_times = []
    simulation_rates = [] # darts thrown per second

    for n in number_of_darts:
        start_time = time()

        pi_approx = throw_darts(n)
        pi_approxs.append(pi_approx)

        execution_time = time() - start_time
        execution_times.append(execution_time)

        simulation_rate = n/execution_time
        simulation_rates.append(simulation_rate)

#         print(f"Number of darts: {n}")
#         print(f"Pi approximation: {pi_approx}")
        print(f"Execution_time (s): {execution_time}")
#         print(f"Darts thrown per second: {n/execution_time} \n")
        
    # Write the number of darts, pi approximations, execution times, 
    #  and simulation rates to a text file
    data = np.column_stack([number_of_darts, pi_approxs, 
                            execution_times, simulation_rates])
    with open("darts_concurrent_futures.txt", "wb") as f:
        np.savetxt(f, data, fmt=['%i','%f', '%f', '%f'])
