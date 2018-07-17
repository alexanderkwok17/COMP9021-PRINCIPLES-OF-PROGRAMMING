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
                return 0, 0, 0 , 0
            tab_string_left.append((table[_].split('->')[0]))
            tab_string_right.append((table[_].split('->')[1]))
            if len(table[_].split('->')[1]) == 0:
                return 0, 0, 0 , 0
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
                    return 0, 0, 0 , 0
        if len(set(token_set)) != table_size[_]:
            print('Token repeated')
            return 0, 0, 0 , 0
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
            return 0, 0, 0 , 0
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
                return 0, 0, 0 , 0
        epsilon.append(epsilon_total_count)

    # -------------------------------------------------------------------------
    epsilon_spot = 0
    for _ in range(len(epsilon)):
        # print('table size = {}'.format(table_size[_]))
        # print('epsilon count = {}'.format(epsilon[_]))
        if epsilon[_] > 0:
            if epsilon[_] != table_size[_]:
                print('Not ALL line is Epsilon')
                return 0, 0, 0 , 0
            if len(RHS_table[_][0]) != 1:
                print('Cant stand with ε')
                return 0, 0, 0 , 0
            epsilon_spot = 1
    return 1, epsilon_spot, LHS_table, RHS_table


def error_message():
    print('Incorrect grammar')


def get_grammar(filename):
    global LHS_ROW_Table, RHS_ROW_Table, LHS_COL_Table, RHS_COL_Table
    switch = 0
    chk_axiom = 0
    chk_row = 0
    chk_col = 0
    column_table = []  # 1
    axiom_array = []  # 2
    row_table = []  # 3
    col_line = 0
    row_line = 0
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
    check_tab_rule_row, epsilon_spot_row, LHS_ROW_Table, RHS_ROW_Table = check_Table_Rule(row_table)
    check_tab_rule_col, epsilon_spot_col, LHS_COL_Table, RHS_COL_Table = check_Table_Rule(column_table)
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
    # print the array
    for _ in range(1, N + 1):
        for i in range(len(print_index)):
            if print_index[i][0] == _:
                print(array[print_index[i][1]])


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
    for _ in range(1, N + 1):
        for i in range(len(print_index)):
            if print_index[i][0] == _:
                print(table[print_index[i][1]])
        if 1 < N != _:
            print('')


grammar = get_grammar('grammar_2_a.txt')
if grammar is not None:
    axiom_array, row_table, column_table = grammar

    print('The axiom array:')
    print_pattern(axiom_array)
    # print(axiom_array)
    print('The row table:')
    print_tables(row_table)
    # print(row_table)
    print('The column Table:')
    print_tables(column_table)
    # print(column_table)
    print('The End')
    non_terminals, terminals = symbol(grammar)
    print(non_terminals)
    print(terminals)

