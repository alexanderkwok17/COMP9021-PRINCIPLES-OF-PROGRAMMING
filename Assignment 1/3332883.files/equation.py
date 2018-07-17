## Solve the equation :
##  abc * de * fg = a * bc * defg
## a to g can be repeated but it is non-zero
## Written by Alexander Kwok for assignment one

# Counter to count how many solutions are there
count = 0
# Set an empty array to store solution
Solution = []
# incremenet each of the variable from 1 to 9:
for a in range(1,10,1):
    for b in range(1,10,1):
        for c in range(1,10,1):
            for d in range(1,10,1):
                for e in range(1,10,1):
                    for f in range(1,10,1):
                        for g in range(1,10,1):
                            # Set each side of the equation to a variable
                            LEFT =  (a*100+b*10+c) *(d*10+e) * (f*10+g)
                            RIGHT = a * (b*10+c) * (d*1000+e*100+f*10+g)
                            # if they equal, we find a SOLUTION!
                            if LEFT == RIGHT:
                                Solution.append ([a,b,c,d,e,f,g])
                                count += 1
print('There are {} solutions:'.format(count))
for i in range(count):
    print('{}{}{} * {}{} * {}{} = '.format(*Solution[i]),end='')
    print('{} * {}{} * {}{}{}{}'.format(*Solution[i]))