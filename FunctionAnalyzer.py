'''
---Function Interpreter---

by David Wilson and Earl Barrowes
(No additional help to cite)

---

Instructions:

1. Click "GO"

2. Enter a function into the input box

Function input rules:
-Use x as the independent variable
-Denote operations using the following symbols: '+' (addition), '-' (subtraction),
'*' (multiplication), '/' (division), '^' exponent
-Decimals are supported (ex. 2.76)
-Note that '-' denotes subtraction; use '_' as a negative sin (ex. _3*x represents -3x)
-Only enter negative signs before numbers or x, not parentheses or trig functions 
(ex. write -(x+2) as _1*(x+2), write -sinx as _1*sinx)
-Always enter the '*' sign; do NOT write numbers/variables/groups next to each other
with no symbol to imply multiplication (ex. write 2*(x+1), NOT 2(x+1))
-Denote trig functions using their appropriate three-letter abbreviations
(sin, cos, tan, csc, sec, cot)
-Parentheses may be used (multiple sets may be used, but not concentric sets)
-Use parentheses and the division symbol for rational functions
-Pi and Euler's number may be denoted using p and e respectively

Example function inputs:
_3*(x-1)^3
7*sin(x+p)
5*x^4-1.3*x^2

3. Enter a closed interval with integer endpoints to use as the domain (separate 
start and end points with a comma and no space)

Example domain inputs:
-1,1
0,5
-10,0

4. Enter a "step" value, which controls the precision of calculations.  Multiples of
ten are recommended.  100 is a good value to start with (the program should run in roughly
30 seconds).  If the program is struggling, try a step of 10, a smaller domain, and/or
a less complex function.

5. The function will then output all local extrema, followed by all absolute extrema.
Note that absolute extrema are also local extrema, and as a result will be list twice.
The function will also output information regarding increasing/decreasing intervals,
concavity, and points of inflection.
'''
"""
Input
"""
from math import sin, cos, tan, pi, e

f_string = input("Please enter function \nf(x) = ") #Gathers function input
domain = input("Please enter a closed interval for the domain (ex. -1,1) ") #Gathers domain input
domain = [int(domain[:domain.index(',')]),int(domain[domain.index(',')+1:])] #Converts domain input to list form
step = int(input('Please enter a "step" value to control the precision of calculations '))

"""
Define f(x)
"""

fl_orig = [] #Defines fl_orig, which will contain items representing the various "pieces" (numbers, x, operations, etc.) of the function

n_test = ['0','1','2','3','4','5','6','7','8','9','10','.'] #List for testing for numbers

i = 0

while i < len(f_string): #Looks through string, examines each item, and adds it to list in the appropriate form
    if f_string[i] in n_test: #Adds multi-digit numbers (ex. 101) as list items
        num = ''
        while i < len(f_string) and f_string[i] in n_test:
            num += f_string[i]
            i += 1
        fl_orig.append(float(num))
    elif f_string[i] in ['s','c','t']: #Adds three-letter representations of trig functions (ex. sin) as list items
        tf = ''
        for x in range(3):
            tf += f_string[i]
            i += 1
        fl_orig.append(tf)
    elif f_string[i] == 'p': #Replaces letter p with decimal representation of pi, adds it to list
        fl_orig.append(pi)
        i += 1
    elif f_string[i] == 'e': #Replaces letter e with decimal representation of Euler's number, adds it to list
        fl_orig.append(e)
        i += 1
    else: #Adds items not in the above categories to list (includes 'x' and operation symbols)
        fl_orig.append(f_string[i])
        i += 1
        
#print(fl_orig) #Delete the hashtag at the beginning of this line if you would like to see the list representing the function

def f(x): #Defines function f
    global fl_orig
    f_list = fl_orig[:] #Creates f_list, a copy of fl_orig (This is done so that the original list remains "intact" and can be reused)
    i = 0
    while i < len(f_list): #Replaces 'x' with numerical value of x
        if f_list[i] == 'x':
            f_list[i] = x
        i += 1
            
    return evaluate(f_list) #Calls the evaluate function to calculate the result - returns this result
    
def evaluate(f_list): #Defines evalute function, which can compute any list using proper order of operates 
    while '_' in f_list: #Eliminates '_' and makes the number immediately after it negative
        i_neg = f_list.index('_')
        f_list = f_list[:i_neg]+[-1*f_list[i_neg+1]]+f_list[i_neg+2:]
    while '(' in f_list: #Searches for parentheses (loops until all parentheses have been eliminated)
        i_open = f_list.index('(')
        i_close = f_list.index(')')
        group = f_list[i_open+1:i_close] #Creates "group," which is a new list consisting of the contents of parentheses
        f_list = f_list[:i_open]+[evaluate(group)]+f_list[i_close+1:] #Calls the evaluate function for "group," and inserts the result into the list where the parentheses and their contents orginally were
    for tf in ['sin','cos','tan','csc','sec','cot']: 
        while tf in f_list: #Looks for trig functions and evaluates all of them until none are left
            t_i = f_list.index(tf)
            if tf == 'sin': #Determines if function is sin - if so, evaluates the sin of the number following the function
                result = sin(f_list[t_i+1])
            elif tf == 'cos': #Repeates for cos and other trig functions
                result = cos(f_list[t_i+1])
            elif tf == 'tan':
                result = tan(f_list[t_i+1])
            elif tf == 'csc':
                result = 1/sin(f_list[t_i+1])
            elif tf == 'sec':
                result = 1/cos(f_list[t_i+1])
            elif tf == 'cot':
                result = 1/tan(f_list[t_i+1])
            f_list = f_list[:t_i]+[result]+f_list[t_i+2:] #Inserts result of trig calculate into list and eliminates original function and number
    while '^' in f_list: #Evaluates all exponents
        op_i = f_list.index('^')
        result = f_list[op_i-1]**f_list[op_i+1] 
        f_list = f_list[:op_i-1]+[result]+f_list[op_i+2:] #Inserts calculated result and eliminates base, exponent symbol, and power
    while '/' in f_list: #Replaces division with multiplication by the recipricol
        i = f_list.index('/')
        f_list[i+1] = 1/f_list[i+1]
        f_list[i] = '*'
    while '*' in f_list: #Evaluates all multiplication (same method as exponents)
        op_i = f_list.index('*')
        result = f_list[op_i-1]*f_list[op_i+1]
        f_list = f_list[:op_i-1]+[result]+f_list[op_i+2:]
    while '-' in f_list: #Replaces subtraction with addition of the opposite
        i = f_list.index('-')
        f_list[i+1] *= -1
        f_list[i] = '+'
    while '+' in f_list: #Evaluates all addition (same method as exponents and multiplication)
        op_i = f_list.index('+')
        result = f_list[op_i-1]+f_list[op_i+1]
        f_list = f_list[:op_i-1]+[result]+f_list[op_i+2:]
    return f_list[0] #List should now contain only one number, which represents the calculated result - function returns this number
    
"""
Calculate f(x), f'(x), f''(x)
"""

calc_precision = 0.0001 #Variable which controls the precision of numerical derivative calculations

x_values = [x/step for x in list(range(domain[0]*step,domain[1]*step+1))] #Defines list of x values which will be used using domain and step

f_data = [] #Creates f_data, a complex list which will hold all calculated values
#Each item in f_data is a smaller 4-item list, consisting of an x value, f(x), f'(x), and f''(x)

fp = lambda x: (f(x+calc_precision)-f(x-calc_precision))/(2*calc_precision) #Defines function for calculating the numerical derivative of a point

for x in x_values:
    f_data.append([x,f(x),fp(x),(fp(x+calc_precision)-fp(x-calc_precision))/(2*calc_precision)]) #Assembles f_data
#f''(x) is calculated by finding the slope between two nearby points on f'(x)
    
#print(f_data) #Remove the hashtag at the beginning of this line if you would like to see f_data
"""
EXTREMA
"""

extrema = [f_data[0][0]]

extrema_i = [0]

for i in range(0,len(f_data)-2): #This line is creating a loop for looking at the values in the funtion
    if f_data[i][2] < 0 and f_data[i+1][2] <= 0 and f_data[i+2][2] > 0: #I am looking at the 3rd term in the list f_data for where it switches signs.
        local_min = f_data[i+1][0]
        print("Local min of "+str(round(f_data[i+1][1],2))+" at x = "+str(f_data[i+1][0]))
        extrema.append(local_min)
        extrema_i.append(i+1)
    elif f_data[i][2] > 0 and f_data[i+1][2] >= 0 and f_data[i+2][2] < 0: #I am looking at the 3rd term in the list f_data for where it switches signs.
        local_max = f_data[i+1][0]
        print("Local max of "+str(round(f_data[i+1][1],2))+" at x = "+str(f_data[i+1][0]))
        extrema.append(local_max)
        extrema_i.append(i+1)
extrema.append(f_data[-1][0])
extrema_i.append(len(f_data))

abs_max = float(f_data[0][1])
abs_max_x = float(f_data[0][0])
abs_min = float(f_data[0][1])
abs_min_x = float(f_data[0][0])

for i in range(0, len(f_data)): #This line is creating a loop for looking at the absolute max and min.
    if float(f_data[i][1]) > abs_max: #This assumes that the first y value of each index is the abs max, if the next y value is higher than the previous one, then it says that the higher value is the new abs max, and this process is repeated until the absolute max is found.
        abs_max = float(f_data[i][1])
        abs_max_x = float(f_data[i][0])
    elif float(f_data[i][1]) < abs_min: #The same process is repeated for the absolute minimum.
        abs_min = float(f_data[i][1])
        abs_min_x = float(f_data[i][0])
        
amax_list = [] #Creates list for absolute extrema in case there is a "tie"
amin_list = []
        
for i in range(0, len(f_data)): #Adds any additional absolute extrema to lists
    if float(f_data[i][1]) == abs_min:
        amin_list.append([float(f_data[i][0]),float(f_data[i][1])])
    if float(f_data[i][1]) == abs_max:
        amax_list.append([float(f_data[i][0]),float(f_data[i][1])])

for m in amax_list: #Prints endpoints as local extrema
    if m[0] == domain[0] or m[0] == domain[1]:
        print("Local max of "+str(round(m[1],2))+" at x = "+str(m[0]))
for m in amin_list:
    if m[0] == domain[0] or m[0] == domain[1]:
        print("Local min of "+str(round(m[1],2))+" at x = "+str(m[0]))

for m in amax_list: #Prints absolute extrema
    print("Absolute max of "+str(round(m[1],2))+" at x = "+str(m[0]))
for m in amin_list:
    print("Absolute min of "+str(round(m[1],2))+" at x = "+str(m[0]))

"""
INC/DEC INTERVALS
"""

for i in range(0,len(extrema)-1): #Creates a loop for looking at the terms
    if f_data[extrema_i[i]+1][2] < 0: #This is looking at where the absolute max/min and the local max/min and 
        print("Decreasing interval on ["+str(extrema[i])+", "+str(extrema[i+1])+"]")
    elif f_data[extrema_i[i]+1][2] > 0: #The same process for increasing intervals.
        print("Increasing interval on ["+str(extrema[i])+", "+str(extrema[i+1])+"]")

"""
POINTS OF INFLECTION
"""

POI = [f_data[0][0]]

POI_i = [0]

for i in range(len(f_data)-2): #Creates a loop to look at the second derivative.
    if f_data[i][3] < 0 and f_data[i+1][3] <= 0 and f_data[i+2][3] > 0: #This looks at where the second derivative switches signs, and when it does is stored in the POI list.
        print("Point of inflection at x = "+str(f_data[i+1][0]))
        POI.append(f_data[i+1][0])
        POI_i.append(i+1)
    elif f_data[i][3] > 0 and f_data[i+1][3] >= 0 and f_data[i+2][3] < 0: #Same process as above, but for the second switch in sign.
        print("Point of inflection at x = "+str(f_data[i+1][0]))
        POI.append(f_data[i+1][0])
        POI_i.append(i+1)
POI.append(f_data[-1][0])
POI_i.append(len(f_data))

"""
CONCAvITY
"""

for i in range(0,len(POI)-1): #Creates a loop to analyze where the POI occur.
    if f_data[POI_i[i]+1][3] < 0: #Looks at where the POI are and say that the interval is between the two POI
        print("Concave down interval on ["+str(POI[i])+", "+str(POI[i+1])+"]")
    elif f_data[POI_i[i]+1][3] > 0: #The same process as above but for other intervals.
        print("Concave up interval on ["+str(POI[i])+", "+str(POI[i+1])+"]")

