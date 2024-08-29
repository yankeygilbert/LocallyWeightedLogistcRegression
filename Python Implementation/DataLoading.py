#loading Data from file x values and y values 

with open("C:\\Users\\yanke\\Downloads\\q2\\data\\x.dat",'r') as x_features:
    content = x_features.readlines()
    x1matrix = [float(line.split()[0]) for line in content] 
    x2matrix = [float(line.split()[1]) for line in content]
   
x_features.close()

with open("C:\\Users\\yanke\\Downloads\\q2\\data\\y.dat",'r') as y_target:
    content = y_target.readlines()
    ymatrix = [float(line.split()[0]) for line in content]

y_target.close()
