"""
We need to give an input of a function and output:
-extrema (max/min, local/absolute)
-inc/dec intervals
-concave up/down
-points of inflection
"""

from math import sin, pi

step = 10
calc_precision = 0.0001

x_values = [x/step for x in list(range(-7*step,7*step+1))]

f_data = []

#fp = lambda a: (sin(a+calc_precision)-sin(a-calc_precision))/(2*calc_precision)
#fp = lambda a: ((a+calc_precision)**2-(a-calc_precision)**2)/(2*calc_precision)
fp = lambda a: ((a+calc_precision)**3-(a+calc_precision)-(((a-calc_precision)**3)-(a-calc_precision)))/(2*calc_precision)

for x in x_values:
    #fp = ((x+calc_precision)**2-(x-calc_precision)**2)/(2*calc_precision)
    #fp = ((x+calc_precision)**3-(x+calc_precision)-(((x-calc_precision)**3)-(x-calc_precision)))/(2*calc_precision)
    #fp = (sin(x+calc_precision)-sin(x-calc_precision))/(2*calc_precision)
    #fpp = (
    f_data.append([x,x**3-x,fp(x),(fp(x+calc_precision)-fp(x-calc_precision))/(2*calc_precision)])
    
print(f_data)
"""
EXTREMA
"""

for i in range(len(f_data)-2):
    if f_data[i][2] < 0 and f_data[i+1][2] <= 0 and f_data[i+2][2] > 0:
        print("Local min at x = "+str(f_data[i+1][0]))
    elif f_data[i][2] > 0 and f_data[i+1][2] >= 0 and f_data[i+2][2] < 0:
        print("Local max at x = "+str(f_data[i+1][0]))
    #else:
    #    print("There are no local max's in the interval")

"""
INC/DEC INTERVALS
"""

d_interval = []
i_interval = []



#for i in range(len(f_data)-2):
#    if f_data[i][2] < 0:
    
for i in range(len(f_data)):
    if f_data[i][2] < 0 and f_data[i+1][2] <= 0 and f_data[i+2][2] > 0:
        d_start = f_data[i][0]
    elif f_data[i][2] > 0 and f_data[i+1][2] >= 0 and f_data[i+2][2] < 0:
        d_stop = f_data[i][0]
    d_interval.append(d_start,d_stop)
#    elif f_data[i][2] > 0 and f_data[i+1][2] > 0:
#        i_interval.append(f_data[i][0])
print("There is a decreasing interval on ["+str(d_interval)+"]")
#print("There is an increasing interval on ["+str(i_interval[0])+", "+str(i_interval[-1])+"]")

"""
CONCAvITY
"""

"""
POINTS OF INFLECTION
"""

for i in range(len(f_data)-2):
    if f_data[i][3] < 0 and f_data[i+1][3] <= 0 and f_data[i+2][3] > 0:
        print("Point of inflection at x = "+str(f_data[i+1][0]))
    elif f_data[i][3] > 0 and f_data[i+1][3] >= 0 and f_data[i+2][3] < 0:
        print("Point of inflection at x = "+str(f_data[i+1][0]))
