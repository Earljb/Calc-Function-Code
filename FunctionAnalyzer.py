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

for i in range(0,len(f_data)-2):
    if f_data[i][2] < 0 and f_data[i+1][2] <= 0 and f_data[i+2][2] > 0:
        print("Local min at x = "+str(f_data[i+1][0]))
    elif f_data[i][2] > 0 and f_data[i+1][2] >= 0 and f_data[i+2][2] < 0:
        print("Local max at x = "+str(f_data[i+1][0]))

abs_max = float(f_data[0][1])
abs_max_x = float(f_data[0][0])
abs_min = float(f_data[0][1])
abs_min_x = float(f_data[0][0])

for i in range(0, len(f_data)):
    if float(f_data[i][1]) > abs_max:
        abs_max = float(f_data[i][1])
        abs_max_x = float(f_data[i][0])
    elif float(f_data[i][1]) < abs_min:
        abs_min = float(f_data[i][1])
        abs_min_x = float(f_data[i][0])

print("There is an absolute max at x = "+str(abs_max_x))
print("There is an absolute min at x = "+str(abs_min_x))

"""
INC/DEC INTERVALS
"""

d_interval = []
i_interval = []

for i in range(0,len(f_data)-2):
    if f_data[i][2] > 0 and f_data[i+1][2] >= 0 and f_data[i+2][2] < 0:
        d_start = f_data[i][0]
    elif f_data[i][2] < 0 and f_data[i+1][2] <= 0 and f_data[i+2][2] > 0:
        d_stop = f_data[i][0]
    d_interval = [d_start,d_stop]
    
for i in range(0,len(f_data)-2):
    if f_data[i][2] < 0 and f_data[i+1][2] <= 0 and f_data[i+2][2] > 0:
        i_start = f_data[i][0]
    elif f_data[i][2] > 0 and f_data[i+1][2] >= 0 and f_data[i+2][2] < 0:
        i_stop = f_data[i][0]
    d_interval = [i_start,i_stop]

#MAKE SURE TO HAVE A WAY TO DO ENDPOINTS


print("There is a decreasing interval on "+str(d_interval))
print("There is an increasing interval on "+str(i_interval))

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
