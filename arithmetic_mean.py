import sys

def arithmetic_mean():
    global valnum
    global vals
    global product
    valnum = raw_input("Number of values: ")
    if valnum == "0":
        valnum = "stop"
    elif valnum == "end":
        sys.exit()
    vals = []
    while True:
        try: 
            valnum = int(valnum)
            break
        except:
            print
            print "Error: Invalid Entry"
            print
            valnum = raw_input("Number of values: ")
            print
    for i in range(valnum):
        val = raw_input("Value " + str(i+1) + ": ")
        while True:
            try:
                val = float(val)
                break
            except:
                print
                print "Error: Invalid Entry"
                print
                val = raw_input("Value " + str(i+1) + ": ")
        vals.append(val)
    summation = 0
    for val in vals:
        summation = float(summation + val)
    product = float(summation/valnum)
    print "Arithmetic Mean: " + str(product)
