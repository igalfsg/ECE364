


vals = input('Please enter some values: ')
vallist = vals.split()
suma =0
for i in vallist:
    try:
       suma +=float(i)
    except (ValueError):
        pass
print ("The sum is: ", suma)