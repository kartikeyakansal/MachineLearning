import numpy as np
import matplotlib
import math
from numpy import loadtxt

#y = mx+c

def gradientdescent(x,y):
    m_orig = 0
    c_orig = 0
    iterations = 500000
    a = 0

    m = len(x)
    learning_rate = 0.0002

    for _ in range(iterations):

        y_calc = m_orig*x + c_orig
        cost_function = (1/(2*m))*sum([val**2 for val in (y-y_calc)])
        if(math.isclose(a,cost_function,rel_tol = 10**-20)):
            break
        a = cost_function
        md = (2/m)* sum((y_calc - y)*x)
        cd = (2/m)* sum(y_calc - y)
        m_orig -= learning_rate*md
        c_orig -= learning_rate*cd
        print("m {} , c {}, cost function {}, iter {}".format(m_orig,c_orig,cost_function,_))
        i = _

    print("m {} , c {}, cost function {}, iter {}".format(m_orig,c_orig,cost_function,i))

x = np.array([92,56,88,70,80,49,65,35,66,67])
y = np.array([98,68,81,80,83,52,66,30,68,73])

gradientdescent(x,y)
