"""
We need to give an input of a function and output:
-extrema (max/min, local/absolute)
-inc/dec intervals
-concave up/down
-points of inflection
"""

"""
term = input("How many terms do you want in your function?")
interval = input("What interval do you want us to analyze?"
"""

step = 100
calc_precision = 0.0001

x_values = [x/step for x in list(range(-3*step,3*step+1))]

f_data = []

for x in x_values:
    fp = ((x+calc_precision)**2-(x-calc_precision)**2)/(2*calc_precision)
    f_data.append([x,x**2,fp])
    
print(f_data)
"""
EXTREMA
"""

for i in range(len(f_data)):
    if f_data[i][2] < 0 and f_data[i+1][2] >= 0:
        print("Local min at "+str(f_data[i][0]))
"""
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

