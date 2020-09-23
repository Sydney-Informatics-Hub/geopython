#https://github.com/PawseySC/Intermediate-Supercomputing/blob/master/darts/serial/python/darts.py
#adapted from pawsey

import numpy.random as rng
import time
import multiprocessing

def pi_run(num_trials):
    """Calculate pi based on points with a box and circle of radius 1
    """
    r = 1.0
    r2 = r * r
    Ncirc = 0
    for _ in range(num_trials):
        x = rng.random() 
        y = rng.random()
        if ( x**2 + y**2 < r2 ):
            Ncirc +=1 
    pi = 4.0 * ( float(Ncirc) / float(num_trials) ) 
    return pi

def cycle_pi():
    """Cycle through a list of trials of increasing magnitude
    """
    num_trials = [10**1,10**2,10**3,10**4,10**5,10**6,10**7]
    pi_estimates = []
    with multiprocessing.Pool() as pool:
        result = pool.map(pi_run,num_trials)
    return result

if __name__ == "__main__":
    start_time = time.time()
    pi = cycle_pi()
    duration = time.time() - start_time
    print(f"Pi convergence : {pi} calculated in {duration} seconds")
