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

step = 1
calc_precision = 0.0001

x_values = [x/step for x in list(range(-3,3*step+1))]

f_data = [[x_values[i],0,0] for i in len(x_values)]
print(f_data)

for x in x_values:
    f = x**2
    print(f,end='  <>  ')
    print(((x+calc_precision)**2-(x-calc_precision)**2)/(2*calc_precision))

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

