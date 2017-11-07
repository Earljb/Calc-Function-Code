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

x_values = [x/step for x in list(range(-3*step,3*step+1))]

f_data = []

for x in x_values:
    fp = ((x+calc_precision)**2-(x-calc_precision)**2)/(2*calc_precision)
    f_data.append([x,x**2,fp])
    #f = x**2
    #print(f,end='  <>  ')
    #print(fp)
    
#f_data = [[x,f,fp] for x in x_values]
print(f_data)
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

