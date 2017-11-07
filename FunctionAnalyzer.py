"""
We need to give an input of a function and output:
-extrema (max/min, local/absolute)
-inc/dec intervals
-concave up/down
-points of inflection
"""

"""
term=input("How many terms do you want in your function?")
"""

"""
EXTREMA
"""

"""
INC/DEC INTERVALS
"""

"""
CONCAvITY
"""

"""
POINTS OF INFLECTION
"""

step = 1
calc_precision = 0.01

x_values = [x/step for x in list(range(0,3*step+1))]

for x in x_values:
    f = x**2
    print(f,end='---')
    #print(((x+calc_precision)**2-(x-calc_precision))/(2*calc_precision))