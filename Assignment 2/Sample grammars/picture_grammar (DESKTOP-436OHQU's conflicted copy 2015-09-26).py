def check_Table_Rule(table):
    LHS_table = []
    RHS_table = []
    tab_string_left = []
    tab_string_right = []
    if table[0] == '':
        tab_count = -2
    else:
        tab_count = -1
    # print('This is table passed:')
    # print(table)
    # -------------------------------------------------------------------------
    # Split the table into Left and right
    for _ in range(len(table)):
        if table[_] != '':
            if table[_].count('->') != 1:
                print('Too many ->')
                return 0, 0, 0 , 0, 0
            tab_string_left.append((table[_].split('->')[0]))
            tab_string_right.append((table[_].split('->')[1]))
            if len(table[_].split('->')[1]) == 0:
                return 0, 0, 0 , 0, 0
        else:
            tab_count += 1
            if tab_count >= 0:
                LHS_table.append(tab_string_left)
                RHS_table.append(tab_string_right)
                tab_string_left = []
                tab_string_right = []
    if  tab_string_left != []:
        LHS_table.append(tab_string_left)
        RHS_table.append(tab_string_right)
    RHS_table = [x for x in RHS_table if x]
    LHS_table = [x for x in LHS_table if x]
    # -------------------------------------------------------------------------
    # Keep note for table size (how many rules within)
    table_size = []
    for _ in range(len(LHS_table)):
        table_size.append(len(LHS_table[_]))
    # -------------------------------------------------------------------------
    # Check valid token
    # First check how many object is on the LHS
    for _ in range(len(LHS_table)):
        for i in range(len(LHS_table[_])):
            LHS_table[_][i] = LHS_table[_][i].split(' ')
    for _ in range(len(LHS_table)):
        for i in range(len(LHS_table[_])):
            for h in range(len(LHS_table[_][i])):
                LHS_table[_][i][h] = LHS_table[_][i][h].replace(' ', '')
            LHS_table[_][i] = [x for x in LHS_table[_][i] if x]
    # Check token can't begin with numbers and can only contain 1 token
    for _ in range(len(LHS_table)):
        token_set = []
        for i in range(len(LHS_table[_])):
                token_set.append(LHS_table[_][i][0])
                if len(LHS_table[_][i]) != 1:
                    print('Can not have zero token')
                    return 0, 0, 0 , 0
                if not (LHS_table[_][i][0][0].isalpha() or  (LHS_table[_][i][0] == '_' and len(LHS_table[_][i]) >1 ) ):
                    print('it is not a valid token')
                    return 0, 0, 0 , 0, 0
        if len(set(token_set)) != table_size[_]:
            print('Token repeated')
            return 0, 0, 0 , 0, 0
    # -------------------------------------------------------------------------
    # Setup RHS List
    for _ in range(len(RHS_table)):
        for i in range(len(RHS_table[_])):
            RHS_table[_][i] = RHS_table[_][i].split(' ')
    for _ in range(len(RHS_table)):
        for i in range(len(RHS_table[_])):
            for h in range(len(RHS_table[_][i])):
                RHS_table[_][i][h] = RHS_table[_][i][h].replace(' ', '')
            RHS_table[_][i] = [x for x in RHS_table[_][i] if x]
    # Test the length consistency
    length_record = []
    for _ in range(len(RHS_table)):
        x = []
        for i in range(len(RHS_table[_])):
            x.append(len(RHS_table[_][i]))
        length_record.append(x)
    for _ in range(len(length_record)):
        if len(set(length_record[_])) != 1:
            print('THe length of RHS is not consistent')
            return 0, 0, 0 , 0, 0
    # -------------------------------------------------------------------------
    # Print out
    # print('table size:')
    # print(table_size)
    # print('LHS:')
    # print(LHS_table)
    # print('RHS:')
    # print(RHS_table)
    # -------------------------------------------------------------------------

    # Check Epsilon occurrence:
    epsilon = []
    for _ in range(len(RHS_table)):
        epsilon_total_count = 0
        for i in range(len(RHS_table[_])):
            epsilon_counter = RHS_table[_][i].count('ε')
            if epsilon_counter > 0:
                epsilon_total_count += epsilon_counter
            if epsilon_counter > 1:  # this check if there is more than 1 ε on each line
                return 0, 0, 0 , 0, 0
        epsilon.append(epsilon_total_count)

    # -------------------------------------------------------------------------
    epsilon_spot = 0
    for _ in range(len(epsilon)):
        # print('table size = {}'.format(table_size[_]))
        # print('epsilon count = {}'.format(epsilon[_]))
        if epsilon[_] > 0:
            if epsilon[_] != table_size[_]:
                print('Not ALL line is Epsilon')
                return 0, 0, 0 , 0, 0
            if len(RHS_table[_][0]) != 1:
                print('Cant stand with ε')
                return 0, 0, 0 , 0, 0
            epsilon_spot = 1
    return 1, epsilon_spot, LHS_table, RHS_table, table_size
def check_axiom(array):
    count_switch = 0
    for _ in range(len(array)):
        if array[_] == '' and array[_-1] != '':
            count_switch += 1
    return count_switch
def error_message():
    print('Incorrect grammar')
def get_grammar(filename):
    global LHS_ROW_Table, RHS_ROW_Table, LHS_COL_Table, RHS_COL_Table, row_table_size, col_table_size
    switch = 0
    chk_axiom = 0
    chk_row = 0
    chk_col = 0
    column_table = []  # 1
    axiom_array = []  # 2
    row_table = []  # 3
    col_line = 0
    row_line = 0
    chk_axiom_array = 0
    # -------------------------------------------------------------------------
    # Read in file by identifying each object
    # 1: column table, 2: Axiom array and 3: row table
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if switch == 1 and line.find('#') == -1:
                column_table.append(line.replace('\n', ''))
                col_line += 1
            elif switch == 2 and line.find('#') == -1:
                axiom_array.append(line.replace('\n', ''))
            elif switch == 3 and line.find('#') == -1:
                row_table.append(line.replace('\n', ''))
                row_line += 1
            if line.find('# Column tables') != -1:
                chk_col += 1
                if line != '\n':
                    switch = 1
            if line.find('# Axiom array') != -1:
                chk_axiom += 1
                if line != '\n':
                    switch = 2
            if line.find('# Row tables') != -1:
                chk_row += 1
                if line != '\n':
                    switch = 3
    # -------------------------------------------------------------------------
    # All stage of Error checking
    if chk_axiom != 1:
        print('missing or too many axiom title')
        error_message()
        return
    if chk_col != 1:
        print('missing or too many col title')
        error_message()
        return
    if chk_row != 1:
        print('missing or too many row title')
        error_message()
        return
    chk_axiom_array =check_axiom(axiom_array)
    check_tab_rule_row, epsilon_spot_row, LHS_ROW_Table, RHS_ROW_Table, row_table_size = check_Table_Rule(row_table)
    check_tab_rule_col, epsilon_spot_col, LHS_COL_Table, RHS_COL_Table, col_table_size = check_Table_Rule(column_table)
    if chk_axiom_array > 1:
        error_message()
        return
    if check_tab_rule_row == 0:
        error_message()
        return
    if check_tab_rule_col == 0:
        error_message()
        return
    if epsilon_spot_row == 1:
        if col_line > 1:
            print(col_line)
            print('ε is in row table, col table must be empty')
            error_message()
            return
    if epsilon_spot_col == 1:
        if row_line > 1:
            print(row_line)
            print('ε is in col table, row table must be empty')
            error_message()
            return
    # -------------------------------------------------------------------------
    # print(axiom_array)
    # print(row_table)
    # print(column_table)
    return axiom_array, row_table, column_table
def symbol(grammar):
    #LHS_ROW_Table, RHS_ROW_Table, LHS_COL_Table, RHS_COL_Table
    # print(LHS_ROW_Table)
    # print(RHS_ROW_Table)
    # print(LHS_COL_Table)
    # print(RHS_COL_Table)
    global non_terminals
    global terminals
    non_terminals = []
    terminals = []
    # Look at LHS first
    for _ in range(len(LHS_ROW_Table)):
        for i in range(len(LHS_ROW_Table[_])):
            for j in range(len(LHS_ROW_Table[_][i])):
                non_terminals.append(LHS_ROW_Table[_][i][j])
    for _ in range(len(LHS_COL_Table)):
        for i in range(len(LHS_COL_Table[_])):
            for j in range(len(LHS_COL_Table[_][i])):
                non_terminals.append(LHS_COL_Table[_][i][j])
    non_terminals = sorted(list(set(non_terminals)))
    # Look at RHS
    for _ in range(len(RHS_ROW_Table)):
        for i in range(len(RHS_ROW_Table[_])):
            for j in range(len(RHS_ROW_Table[_][i])):
                terminals.append(RHS_ROW_Table[_][i][j])
    for _ in range(len(RHS_COL_Table)):
        for i in range(len(RHS_COL_Table[_])):
            for j in range(len(RHS_COL_Table[_][i])):
                terminals.append(RHS_COL_Table[_][i][j])
    terminals = sorted(list(set(terminals)- set(non_terminals)))
    return non_terminals, terminals
def print_pattern(array):
    print_index = []
    N = 0
    # Extract non empty lines
    for _ in range(len(array)):
        if _ > 0:
            if len(array[_]) != 0 and len(array[_ - 1]) == 0:
                N += 1
            if N > 0 and len(array[_]) != 0:
                print_index.append([N, _])
        if _ == 0:
            if len(array[_]) != 0:
                N += 1
            if N > 0 and len(array[_]) != 0:
                print_index.append([N, _])
    # print(print_index)
    # # print the array
    # for _ in range(1, N + 1):
    #     for i in range(len(print_index)):
    #         if print_index[i][0] == _:
    #             print(array[print_index[i][1]])
    Temp = []
    for _ in range(1, N + 1):
        for i in range(len(print_index)):
            if print_index[i][0] == _:
                Temp.append(array[print_index[i][1]].split(' '))
        if 1 < N != _:
            Temp.append('\n')
            # print('')
    for _ in range(len(Temp)):
        Temp[_] = list(filter(None,Temp[_]))
    max_length = []
    m = 0
    start = 1
    for _ in range(len(Temp[0])):
        max_length.append(len(Temp[0][_]))
    for _ in range(len(Temp)):
        for i in range(len(Temp[_])):
            if start == 0:
                print('{:<1}'.format(Temp[_][i]),end='')
                if len(Temp[_])>1 and m < len(max_length)-1:
                    print(' ',end='')
            else:
                start = 0
                print('{:<1}'.format(Temp[_][i]),end='')
                if len(Temp[_])>1:
                    print(' ',end='')
            if len(Temp[_][i]) < max_length[m]:
                if m < len(max_length)-1:
                    for j in range(max_length[m] - Temp[_][i]):
                        print(' ',end='')
            m += 1
            if m > len(max_length)-1:
                m = 0
        print('')
        start = 1
    global array_Temp
    array_Temp = Temp
def print_tables(table):
    print_index = []
    N = 0
    # Extract the non empty lines
    for _ in range(len(table)):
        if _ > 0:
            if len(table[_]) != 0 and len(table[_ - 1]) == 0:
                N += 1
            if N > 0 and len(table[_]) != 0:
                print_index.append([N, _])
        if _ == 0:
            if len(table[_]) != 0:
                N += 1
            if N > 0 and len(table[_]) != 0:
                print_index.append([N, _])
    # print(print_index)
    # print(table[3][0])
    # Sort the rules into lexi order
    for _ in range(1, N + 1):
        start = 100
        end = 0
        for i in range(len(print_index)):
            if print_index[i][0] == _:
                start = min(start, print_index[i][1])
                end = max(end, print_index[i][1])
        table[start:end + 1] = sorted(table[start:end + 1])
    # Print the rules by blocks
    Temp = []
    for _ in range(1, N + 1):
        for i in range(len(print_index)):
            if print_index[i][0] == _:
                Temp.append(table[print_index[i][1]].split(' '))
        if 1 < N != _:
            Temp.append('\n')
            # print('')
    for _ in range(len(Temp)):
        Temp[_] = list(filter(None,Temp[_]))
    # find max_length for each position
    max_length = []
    next_rule = 0
    tab_count = 0
    line_one = 1
    max_length_store = []
    m = 0
    for _ in range(len(Temp)):
        if Temp[_][0] == '\n':
            tab_count += 1
            line_one = 1
            next_rule = 0
            continue
        # for each rule
        for i in range(len(Temp[_])):
            if line_one == 1:
                #print('LINE ONE : {}'.format(Temp[_][i]),end='')
                max_length_store.append(len(Temp[_][i]))
                next_rule += 1
            else:
                #print(max_length,tab_count,m,max_length[tab_count][m] )
                if max_length[tab_count][m] < len(Temp[_][i]):
                    max_length[tab_count][m] = len(Temp[_][i])
                m += 1
                #print(Temp[_][i],end = '')
                if m == next_rule:
                    m = 0
        if line_one == 1:
            max_length.append(max_length_store)
            max_length_store= []
        #print('')
        line_one = 0
    # start printing table
    count_item = 0
    tab_count = 0
    start = 1
    #print(max_length)
    for _ in range(len(Temp)):
        if Temp[_][0] == '\n':
            tab_count += 1
        for i in range(len(Temp[_])):
            if Temp[_][i] != '\n':
                if Temp[_][i] != '->':
                    if Temp[_][i] == 'ε':
                        print('',end='')
                    else:
                        if start == 0:
                            print(' {:<1}'.format(Temp[_][i]),end='')
                        else:
                            start = 0
                            print('{:<1} '.format(Temp[_][i]),end='')
                    if len(Temp[_][i]) < max_length[tab_count][count_item]:
                         if count_item < len(max_length[tab_count])-1:
                             for m in range(max_length[tab_count][count_item] - len(Temp[_][i]) ):
                                print(' ',end='')
                    count_item += 1
                    if count_item  > len(max_length[tab_count])-1:
                        count_item = 0
                else:
                    count_item += 1
                    if count_item  > len(max_length[tab_count])-1:
                        count_item = 0
                    if Temp[_][i] == 'ε':
                        print('',end='')
                    else:
                        print('{:>1}'.format(Temp[_][i]),end='')

            # if arrow == 1:
            #     print('x',end='')
        print('')
        start = 1

    # print('----------------------\nEND')
def generate(grammar,picture):
    # Print out each step
    from copy import deepcopy
    import itertools
    def print_picture(array_Temp):
        first_one = 1
        for _ in range(len(array_Temp)):
            for i in range(len(array_Temp[_])):
                if first_one == 1:
                    first_one = 0
                    print('{}'.format(array_Temp[_][i]),end ='')
                else:
                    print(' {}'.format(array_Temp[_][i]),end ='')
            print('')
            first_one = 1
    # Apply the rule
    def apply_col_tab(col_tab,original):
        reconstruct = 0
        axiom = deepcopy(original)
        new_axiom = []
        first = 1
        count = 0
        # print('-'*10)
        # print('OLD:',axiom)
        for _ in range(len(axiom)):
            for i in range(len(axiom[_])):
                # print(axiom[_][i], _, i,end='')
                axiom[_][i] = col_tab.get(axiom[_][i],axiom[_][i])
                # print(axiom[_][i], _, i)
        for _ in range(len(axiom)):
            for i in range(len(axiom[_])):
                if ' ' in axiom[_][i]:
                    reconstruct = 1
        # if reconstruct == 1:
        # print('NEW:',original)
        for _ in range(len(axiom)):
                for i in range(len(axiom[_])):
                    # print(axiom[_][i])
                    if first == 1 :
                        first = 0
                        if len(axiom[_][i].split(' ')) > 1:
                            new_axiom.append([axiom[_][i].split(' ')[0]])
                            for m in range(1,len(axiom[_][i].split(' '))):
                                new_axiom[count].append(axiom[_][i].split(' ')[m])
                        else:
                            new_axiom.append([axiom[_][i]])
                    else:
                        for m in range(len(axiom[_][i].split(' '))):
                            new_axiom[count].append(axiom[_][i].split(' ')[m])
                    # print(new_axiom)
                first = 1
                count += 1
        # print('--'*10)
        return new_axiom
    global array_Temp
    axiom_array, row_table, column_table = grammar
    # Get axiom size first,Update for every transform
    min_col = len(array_Temp[0])
    min_row = len(array_Temp)
    # print('Minimum row is {}'.format(min_row))
    # print('Minimum col is {}'.format(min_col))
    # Get picture size
    # Validate the picture
    count_row = 0
    pic_col_size = []
    pic_row_size = 1
    new_row = 0
    for _ in range(len(picture)):
        if picture[_] == '\n':
            pic_row_size += 1
            new_row = 1
        if new_row == 1 and picture[_] != '\n':
            pic_col_size.append(count_row)
            count_row = 0
            new_row = 0
        if picture[_] != '\n':
            count_row += 1
    pic_col_size.append(count_row)
    # Cannot generate picture if its row inconsistent
    if len(set(pic_col_size)) != 1:
        print('Picture cannot be generated.')
        return
    # Picture is invalid as it has less row than the axiom array
    if pic_col_size[0] < min_col or pic_row_size < min_row:
        print('Picture is invalid.')
        return
    # print('The col size of the picture is {}.'.format(pic_col_size[0]))
    # print('The row size of the picture is {}.'.format(pic_row_size))
    row_dict = []
    col_dict = []
    count_tab = 0
    temp_dict = {}
    # print(row_table)
    # print(column_table)
    for _ in range(len(row_table)):
        # print('STEP {}'.format(_))
        if row_table[_] != '':
            LHS = row_table[_].split('->')[0].replace(' ','')
            RHS = row_table[_].split('->')[1]
            while RHS[0] == ' ':
                RHS = RHS[1:]
            while RHS[len(RHS)-1] == ' ':
                RHS = RHS[0:len(RHS)-2]
            # print(LHS, RHS)
            temp_dict[LHS] = RHS
            # print(_,temp_dict)
        else:
            row_dict.append(temp_dict.copy())
            # print(row_dict)
            temp_dict.clear()
            count_tab += 1
    row_dict.append(temp_dict.copy())
    count_tab = 0
    # print(column_table)
    for _ in range(len(column_table)):
        # print('lOPP {}'.format(_))
        if column_table[_] != '':
            # print('in first')
            LHS = column_table[_].split('->')[0].replace(' ','')
            RHS = column_table[_].split('->')[1]
            while RHS[0] == ' ':
                RHS = RHS[1:]
            while RHS[len(RHS)-1] == ' ':
                RHS = RHS[0:len(RHS)-2]
            temp_dict[LHS] = RHS
        else:
            #print('in second')
            #if count_tab != 0:
                # print(temp_dict)
                # print('---'*10)
                col_dict.append(temp_dict.copy())
                # print(col_dict)
                temp_dict.clear()
                identify = 1
                count_tab += 1
        # print(col_dict)
    col_dict.append(temp_dict.copy())
    # Remove empty dict
    row_dict[:] = [x for x in row_dict if not len(x) == 0]
    col_dict[:] = [x for x in col_dict if not len(x) == 0]
    # print('Row IS :',row_dict)
    # print('Col IS :',col_dict)
    # print(picture)
    # print(array_Temp)
    # picture size
    # pic_col_size[0]
    # pic_row_size
    # Current expanded axiom size
    chk_pic = []
    new_line = 1
    count = -1
    for _ in range(len(picture)):
        if picture[_] != '\n':
            if new_line == 1:
                new_line = 0
                chk_pic.append([picture[_]])
                count += 1
            else:
                chk_pic[count].append(picture[_])
        else:
            new_line = 1
    # print('--------'*10)
    # Start with initial PiC generate all possible one step picture on if it is smaller than the PICTURE
    store_pic = [deepcopy(array_Temp)]
    store_pic_next = []
    # print(store_pic)
    x = 0
    remove_string = []
    new_store_pic = []
    uniq_new_store_pic = []
    parent_string = []
    match_count = 0
    store_move = []
    current_move = []
    forward_check = []
    fail_check = 0
    answer_move = []
    new_store_move = []
    new_current_move = []
    steps = []
    count_terminal = 0
    count_all = 0
########################################################################################################################
#  METHOD 2
#     print(store_pic[0])
    stop = 0
    force_stop = 0
    while  stop != 1 and force_stop != 1:  #x < 2: # and
        print(x)
        # print('Step {}'.format(x))
        # print('---------------------')
        # print('Store Pic', len(store_pic))
        # for _ in range(len(store_pic)//10):
        #     print(store_pic[_])
        # print('Store Move',len(store_move))
        # for _ in range(len(store_move)//10):
        #     print(store_move[_])
        # print('---------------------')
        x += 1
        for i in range(len(store_pic)):
            # print('{}th in store pic'.format(i))
            for _ in range(len(col_dict)):
                ############# CHECK IF PICTURE IS VALID BEFORE ADDING IN  ##################
                forward_check = apply_col_tab(col_dict[_], store_pic[i])
                check = len(forward_check[0])
                for m in range(len(forward_check)):
                    # this is for checking constant row size
                    if len(forward_check[m]) != check:
                        fail_check = 1
                    # THIS IS for pic size larger than requested pic
                    if len(forward_check[m]) > pic_col_size[0] or len(forward_check) > pic_row_size:
                        fail_check = 1
                    # IF all terminals, then if its not matching the size of pic it can be dumped
                    for k in range(len(forward_check[m])):
                        if forward_check[m][k] in terminals:
                            count_terminal += 1
                        count_all += 1
                    if count_terminal == count_all:
                        if len(forward_check[m]) != pic_col_size[0] or len(forward_check) != pic_row_size:
                            fail_check = 1
                    count_terminal = 0
                    count_all = 0
                if fail_check == 0:
                    ########## NOW ADD IN THE PICTURE ##################################
                    store_pic_next.append(apply_col_tab(col_dict[_], store_pic[i]))
                    if len(store_move) != 0:
                        temp_move = deepcopy(store_move[i])
                        temp_move.append(['C', _])
                        current_move.append(deepcopy(temp_move))
                        temp_move.clear()
                    else:
                        current_move.append([['C', _]])
                    ####### ADD IN ENDS HERE  ################################
                fail_check = 0
            for _ in range(len(row_dict)):
                ############# CHECK IF PICTURE IS VALID BEFORE ADDING IN  ##################
                chk_Temp = apply_col_tab(row_dict[_], list(map(list, zip(*store_pic[i]))))
                forward_check = list(map(list, zip(*chk_Temp)))
                check = len(forward_check[0])
                for m in range(len(forward_check)):
                    if len(forward_check[m]) != check:
                        fail_check = 1
                    if len(forward_check[m]) > pic_col_size[0] or len(forward_check) > pic_row_size:
                        fail_check = 1
                    for k in range(len(forward_check[m])):
                        if forward_check[m][k] in terminals:
                            count_terminal += 1
                        count_all += 1
                    if count_terminal == count_all:
                        if len(forward_check[m]) != pic_col_size[0] or len(forward_check) != pic_row_size:
                            fail_check = 1
                    count_terminal = 0
                    count_all = 0
                if fail_check == 0:
                    ########## NOW ADD IN THE PICTURE ##################################
                    Temp = apply_col_tab(row_dict[_], list(map(list, zip(*store_pic[i]))))
                    store_pic_next.append(list(map(list, zip(*Temp))))
                    if len(store_move) != 0:
                        temp_move = deepcopy(store_move[i])
                        temp_move.append(['R', _])
                        current_move.append(deepcopy(temp_move))
                        temp_move.clear()
                    else:
                        current_move.append([['R', _]])
                    ####### ADD IN ENDS HERE  ################################
                fail_check = 0
            # for _ in range(len(store_pic_next)):
            #     print(store_pic_next[_],'Move:',current_move[_])
        store_pic = deepcopy(store_pic_next)
        store_move = deepcopy(current_move)
        store_pic_next.clear()
        current_move.clear()
        for _ in range(len(store_pic)):
            if chk_pic ==  store_pic[_]:
                print('FOUND IT')
                print(store_pic[_])
                print(store_move[_])
                match_count += 1
        if match_count == 1:
            pass
            # stop = 1
        if match_count > 1:
            force_stop = 1
        match_count = 0


    return
########################################################################################################################
    while len(store_pic) != 0 and match_count < 1 :#
        x += 1
        # print('----STEP {}'.format(x))
########################################################################################################################
        # check what's it start with
        # print('----------'*10)
        # print('this is the item in the old list:')
        # for i in range(len(store_pic)):
        #     print(store_pic[i])
        # print('----------'*10)
########################################################################################################################
        # m will be zero on first iteration, then become more as the tree expand
        for m in range(len(store_pic)):
            parent_string.append(store_pic[m])
            # print('----M STEP {}'.format(m))
            # for k in range(len(store_pic)):
            #     print(store_pic[k])
            # print(len(store_pic))
            # print(store_pic[m])
            for i in range(len(col_dict)):
                # check if the generated picture is valid
                forward_check = apply_col_tab(col_dict[i],store_pic[m])
                check = len(forward_check[0])
                for _ in range(len(forward_check)):
                    # print(len(forward_check[_]),forward_check[_] , check, forward_check[0])
                    if len(forward_check[_]) != check:
                        fail_check = 1

                if store_pic[m] != apply_col_tab(col_dict[i],store_pic[m]) and fail_check != 1:
                    store_pic_next.append(apply_col_tab(col_dict[i],store_pic[m]))
                fail_check = 0
            fail_check = 0
            for i in range(len(row_dict)):
                chk_Temp = apply_col_tab(row_dict[i],list(map(list, zip(*store_pic[m]))))
                forward_check = list(map(list, zip(*chk_Temp)))
                check = len(forward_check[0])
                for _ in range(len(forward_check)):
                    # print(len(forward_check[_]),forward_check[_] , check, forward_check[0])
                    if len(forward_check[_]) != check:
                        fail_check = 1

                if store_pic[m] != list(map(list, zip(*apply_col_tab(row_dict[i],list(map(list, zip(*store_pic[m]))))))) and fail_check != 1:
                    Temp = apply_col_tab(row_dict[i],list(map(list, zip(*store_pic[m]))))
                # print_picture(list(map(list, zip(*Temp))))
                    store_pic_next.append(list(map(list, zip(*Temp))))
                fail_check = 0
            new_store_pic.append([l for l in store_pic_next if l not in remove_string])
            store_pic_next.clear()

        # print('This is each item inside the new list')
        # for i in range(len(new_store_pic)):
        #         print(new_store_pic[i])
        # print('This is the whole list')
        # print(new_store_pic)
        for i in range(len(store_pic)):
            remove_string.append(store_pic[i])
        store_pic.clear()
        for i in range(len(new_store_pic)):
            for m in range(len(new_store_pic[i])):
                store_pic.append(new_store_pic[i][m])
        # print('---------------')
        # print(store_pic)
        # store_pic = deepcopy(new_store_pic)
        new_store_pic.clear()
        # print('---------'*10)
        for i in range(len(store_pic)):
            # print(store_pic[i])
            # print(chk_pic)
            if store_pic[i] == chk_pic:
                # print(x)
                match_count += 1
                steps.append(x)
                # print(store_pic)
                remove_string.append(store_pic[i])
        # Remove image with all terminals if it does not match
        for i in range(len(store_pic)):
            if len(store_pic[i]) > pic_row_size or len(store_pic[i][0]) > pic_col_size[0] :
                remove_string.append(store_pic[i])
            chk_count = 0
            len_count = 0
            for m in range(len(store_pic[i])):
                for n in range(len(store_pic[i][m])):
                    if store_pic[i][m][n] in terminals:
                        chk_count += 1
                    len_count += 1
            if chk_count == len_count:
                if store_pic[i] != chk_pic:
                    remove_string.append(store_pic[i])
        store_pic = [l for l in store_pic if l not in remove_string]
        # Add the one that is too big in to the remove list
        # for i in range(len(new_store_pic)):

        # Take out duplicated ones
        # for i in range(len(new_store_pic)):
        #     for m in range(len(new_store_pic[i])):
        #         # dont add if it larger than the picture
        #         if pic_col_size[0] >= len(new_store_pic[i][m][0]) and pic_row_size >= len(new_store_pic[i][m]):
        #             if new_store_pic[i][m] not in uniq_new_store_pic:
        #                 if new_store_pic[i][m] not in store_pic:
        #                     # print('added:', new_store_pic[i][m])
        #                     uniq_new_store_pic.append(new_store_pic[i][m])
        # new_store_pic.clear()
        # # Take out duplicated ones from previous list:
        # for i in range(len(store_pic)):
        #     if store_pic[i] in uniq_new_store_pic:
        #         # print('Removed:',store_pic[i])
        #         uniq_new_store_pic.remove(store_pic[i])
        # # Remove parent image
        # for i in range(len(parent_string)):
        #     if parent_string[i] in uniq_new_store_pic :
        #         uniq_new_store_pic.remove(parent_string[i])
        # # Remove image with all terminals if it does not match
        # for i in range(len(uniq_new_store_pic)):
        #     chk_count = 0
        #     len_count = 0
        #     for m in range(len(uniq_new_store_pic[i])):
        #         for n in range(len(uniq_new_store_pic[i][m])):
        #             if uniq_new_store_pic[i][m][n] in terminals:
        #                 chk_count += 1
        #             len_count += 1
        #     if chk_count == len_count:
        #         if uniq_new_store_pic[i] != chk_pic:
        #             remove_string.append(uniq_new_store_pic[i])
        # print('This is each item inside the new list')
        # for i in range(len(uniq_new_store_pic)):
        #         print(uniq_new_store_pic[i])
        # print('This is the whole list')
        # print(uniq_new_store_pic)
        # store_pic = deepcopy(uniq_new_store_pic)
        # uniq_new_store_pic.clear()
        # print('---------'*10)
        # for i in range(len(store_pic)):
        #     # print(store_pic[i])
        #     # print(chk_pic)
        #     if store_pic[i] == chk_pic:
        #         match_count += 1
        #         steps.append(x)
    # print('--------------------------WORK STARTS HERE ------------------------------------')
    # print('Steps takes:',steps)
    options = []
    original_options = []
    count_match = 0
    for _ in range(len(row_dict)):
        options.append(['R',_])
    for _ in range(len(col_dict)):
        options.append(['C',_])
    original_options = deepcopy(options)
    options = list(itertools.product(options, repeat = min(steps)))
    store_pic = deepcopy(array_Temp)
    # print(len(options))
    for _ in range(len(options)):
        for i in range(len(options[_])):
            if options[_][i][0] == 'R':
                    Temp = apply_col_tab(row_dict[options[_][i][1]],list(map(list, zip(*store_pic))))
                    store_pic = (list(map(list, zip(*Temp))))
            elif options[_][i][0] == 'C':
                    store_pic = apply_col_tab(col_dict[options[_][i][1]],store_pic)
            if len(store_pic) > pic_row_size or len(store_pic[0]) > pic_col_size[0] :
                    break
        # ENd one simulation
        if store_pic == chk_pic:
            # print('YES')
            count_match +=  1
            # print('{} simulation:'.format(_))
            path = options[_]
            # print(options[_])
            # print(store_pic)
            # print('------------------------')
            # print(len(steps))
            break
        # now check if its equal to chk_pic
        store_pic = deepcopy(array_Temp)
    # TEst for longer non-deterministic path

    # print(chk_pic)
    # print('THIS IS COUNT MATCH: {}'.format(count_match))
    if match_count == 1:
        end = 0
        print('Picture can be generated in only one way.')
        print('Here it is:')
        print_picture(array_Temp)
        print('')
        store_pic = deepcopy(array_Temp)
        for i in range(len(path)):
            if path[i][0] == 'R':
                    Temp = apply_col_tab(row_dict[path[i][1]],list(map(list, zip(*store_pic))))
                    store_pic = (list(map(list, zip(*Temp))))
                    print_picture(store_pic)
            elif path[i][0] == 'C':
                store_pic = apply_col_tab(col_dict[path[i][1]],store_pic)
                print_picture(store_pic)
            if i == len(path) - 1 :
                end = 1
            if end != 1:
                print('')
    if match_count > 1:
        print('Picture cannot be generated in only one way.')
        print('Here is the final deterministic part:')


    return

grammar = get_grammar('grammar_2_b.txt')
if grammar is not None:
    axiom_array, row_table, column_table = grammar
    # print(axiom_array)
    print('The axiom array:')
    print_pattern(axiom_array)
    # print(row_table)
    print('The row table:')
    print_tables(row_table)
    # print(column_table)
    print('The column Table:')
    print_tables(column_table)

    non_terminals, terminals = symbol(grammar)
    print('Non Terminals:')
    print(non_terminals)
    print('Terminals:')
    print(terminals)
    print('Generate Picture:')
    generate(grammar,'ababa\nbabab\nababa\nbabab\nababa')
    # Other picture
    # aSa
    # aaaaaaa\nbbbabbb\nbbbabbb
    # aaaaaaa\nbbbabbb\nbbbabbb\nbbbabbb
    # grammar 2 test:
    # ababa\nbabab\nababa\nbabab\nababa
    #
    # ***\n***\n***