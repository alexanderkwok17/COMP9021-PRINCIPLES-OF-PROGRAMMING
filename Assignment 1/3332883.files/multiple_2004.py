# Take the obvious upper bound for both A and B
# A = 2004 and B = 2004
# Hence N is  200420042004 = 2004 * 100010001
# Then we can start searching from the lower bound
N = 200420042004
Solution = []
# First search for the each A with all B, and store the solution if it's less than N
for A in range(1, 2004, 1):
    for B in range(1, 2004, 1):
        current = int(str(A) + '2004' + str(B))
        if current % 2004 == 0:
            # if its divisible by 2004 and less than N (the potential solution)
            # then it can replace the current solution
            if N > current:
                N = current
                Solution = [A, B, current]
        # Now try for the reverse position,
        # where the put B as the location of A
        # and A as the location of B
        # So that we can test out if there will be a smaller solution
        current = int(str(B) + '2004' + str(A))
        # Again, replace the current solution if its less than N
        if current % 2004 == 0:
            if N > current:
                N = current
                Solution = [B, A, current]
# The final N would be replaced by the smallest possible solution:
print('A = {}, B = {}, N = {} is the solution.'.format(*Solution))