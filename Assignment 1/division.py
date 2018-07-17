# To find the solution of the long division
#  * * * * a * * | * a * =  n_1 a n_2  = Divisor
#  (  i  ) a     |
#                | --------
#  * * a a=mult_1| * * a * = q_1 q_2 a q_3  (where mult_1 = Divisor * q_1 )
#  -------       |
#  * * * a = (i - mult_1) with an a
#    * * a = Mult_2 = Divisor * q_2
#    -----
#    * * * * =  * * * m = str(***a - mult_2) + str(m)
#    * a * * = mult_3 = Divisor * a
#    -------
#    * * * * = * * * o = str(***m - mult_3) + str(o)
#    * * * * = Mult_4 = Divisor * q_3
#    -------
#          0
#   as the remainder is 0, we can use the condition where
#    Mult_4 = str(***m - mult_3) + str(o)
#   Hence we have developed the function test_case to check this condition:

# This functions check all possible multiplication
# which gives the exact same value as multiple 4 ( = Divisor * q_3)
def test_case(mult_1, mult_2, mult_3, mult_4):
    for i in range(1000, 9999, 1): # First loop the first part using i the 4 digit number
        if i - mult_1 > 99: # since i the 4 digit number from the first part of ****a**
            # the remainder is a 3 digit number so i- mult_1 is > 99
            for m in range(10):
                for o in range(10):
                    if int(str(i - mult_1)[1]) != a:
                    # now str(i - mult_1) + str(a) is ***a
                    # and ***a - mult_2 is  the remainder ***m (where m is another *)
                    # and so ***m - mult_3 is the remainder ***o (where o is another *)
                    # Finally, the solution is found when
                    # ***o = mult_4 as zero is the final remainder.
                        if int(str(int(str(int(str(i - mult_1) + str(a)) - mult_2) + str(m)) - mult_3) + \
                                       str(o)) == mult_4:
                            quotient = int(str(q_1) + str(q_2) + str(a) + str(q_3))
                            Solution = [Divisor * quotient, Divisor, quotient]
                            print('{} / {} = {} is the solution.'.format(*Solution))


# First set the loop for the a ( and since all * can't be a we use the if
# statement to skip all * equals to a.
for a in range(10):
    for n_1 in range(1, 10, 1):  # Use n_1 and n_2 to represent the Parts of Divisor = n_1,a,n_2
        if n_1 != a:
            for n_2 in range(10):
                if n_2 != a:
                    Divisor = int(str(n_1) + str(a) + str(n_2))  # combine the digit to get the divisor
                    for q_1 in range(1, 10, 1): # let q_1 be the the first * of **a* so that it
                        # will give us the first multiple of the divisor
                        if q_1 != a and Divisor * q_1 > 999:
                            mult_1 = Divisor * q_1
                            # Using the hints from the question, the 3rd and 4th digit equal to a
                            if str(mult_1)[2] == str(mult_1)[3] and int(str(mult_1)[2]) == a and int(
                                    str(mult_1)[1]) != a and int(str(mult_1)[0]) != a:
                                for q_2 in range(1, 10, 1): # let q_2 be the second * of **a*
                                    if q_2 != a:
                                        mult_2 = Divisor * q_2
                                        # same idea, the 3rd digit of multiple 2 is a
                                        # but the other two cannot be a
                                        if int(str(mult_2)[2]) == a and int(str(mult_2)[0]) != a and int(
                                                str(mult_2)[1]) != a:
                                            for q_3 in range(1, 10, 1): # now let q_3 be the final * in **a*
                                                if q_3 != a and Divisor * q_3 > 999:
                                                    # As q_3 can't be a and
                                                    # the multiple of Divisor and q_3 is 4 digit
                                                    # the above if statement filters out the correct answer
                                                    mult_4 = Divisor * q_3
                                                    mult_3 = Divisor * a
                                                    # Now as 2nd digit of multiple 3 is a
                                                    # and we know that all other digit cannot be a
                                                    # so the remaining cases will be the possible solution
                                                    if int(str(mult_3)[1]) == a and int(str(mult_4)[0]) != a \
                                                            and int(str(mult_4)[1]) != a and int(str(mult_4)[2]) != a \
                                                            and int(str(mult_4)[3]) != a:
                                                        test_case(mult_1, mult_2, mult_3, mult_4)
