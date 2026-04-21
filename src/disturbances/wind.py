import numpy as np

def wind(t):
    return 0.3*np.sin(0.2*t) + 0.1*np.sin(1.5*t)