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

extrema = [f_data[0][0]]

extrema_i = [0]

for i in range(0,len(f_data)-2):
    if f_data[i][2] < 0 and f_data[i+1][2] <= 0 and f_data[i+2][2] > 0:
        local_min = f_data[i+1][0]
        print("Local min at x = "+str(f_data[i+1][0]))
        extrema.append(local_min)
        extrema_i.append(i+1)
    elif f_data[i][2] > 0 and f_data[i+1][2] >= 0 and f_data[i+2][2] < 0:
        local_max = f_data[i+1][0]
        print("Local max at x = "+str(f_data[i+1][0]))
        extrema.append(local_max)
        extrema_i.append(i+1)
extrema.append(f_data[-1][0])
extrema_i.append(len(f_data))

print(str(extrema_i))
print(str(extrema))

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

for i in range(0,len(extrema)-1):
    if f_data[extrema_i[i]+1][2] < 0:
        print("There is a decreasing interval on ["+str(extrema[i])+", "+str(extrema[i+1])+"]")
    elif f_data[extrema_i[i]+1][2] > 0:
        print("There is a increasing interval on ["+str(extrema[i])+", "+str(extrema[i+1])+"]")

"""
POINTS OF INFLECTION
"""

POI = [f_data[0][0]]

POI_i = [0]

for i in range(len(f_data)-2):
    if f_data[i][3] < 0 and f_data[i+1][3] <= 0 and f_data[i+2][3] > 0:
        print("Point of inflection at x = "+str(f_data[i+1][0]))
        POI.append(f_data[i+1][0])
        POI_i.append(f_data[i+1][0])
    elif f_data[i][3] > 0 and f_data[i+1][3] >= 0 and f_data[i+2][3] < 0:
        print("Point of inflection at x = "+str(f_data[i+1][0]))
        POI.append(f_data[i+1][0])
        POI_i.append(f_data[i+1][0])
POI.append(f_data[-1][0])
POI_i.append(len(f_data)

"""
CONCAvITY
"""

for i in range(0,len(extrema)-1):
    print(str(extrema_i[i]+1))
    if f_data[extrema_i[i]+1][3] < 0:
        print("There is a concave down interval on ["+str(extrema[i])+", "+str(extrema[i+1])+"]")
    elif f_data[extrema_i[i]+1][3] > 0:
        print("There is a concave up interval on ["+str(extrema[i])+", "+str(extrema[i+1])+"]")

