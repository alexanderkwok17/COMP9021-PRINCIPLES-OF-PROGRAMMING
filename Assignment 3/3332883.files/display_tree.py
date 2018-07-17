import sys
import os
Argument = []
for _ in range(len(sys.argv)):
    if _ != 0:
        Argument.append(sys.argv[_])


# print( 'Number of arguments:', len(sys.argv), 'arguments.')
# print( 'Argument List:', str(sys.argv))
# print('------\n This is what you put in:')
# print(Argument)
grow = ''
nodestyle = ''
valid = ['-grow', '-nodestyle']
valid_grow = ['up','down','left','right']
valid_nodestyle = ['rectangle','circle','ellipse']
filename = ''
count_grow = 0
count_nodestyle = 0
error = 0
for _ in range(len(Argument)):
    if '.txt' in Argument[_]:
        if _ != len(Argument)- 1:
            print('Incorrect invocation')
            error = 1
            break
        filename = Argument[_]
    if '-grow' in Argument[_]:
        if Argument[_+1] not in valid_grow:
            print('Incorrect invocation')
            error = 1
            break
        grow = "[grow'=" + Argument[_+1] + ']'
        count_grow += 1
        if count_grow > 1:
            print('Incorrect invocation')
            error = 1
            break
    if '-nodestyle' in Argument[_]:
        if Argument[_+1] not in valid_nodestyle:
            print('Incorrect invocation')
            error = 1
            break
        nodestyle = "\\tikzstyle{every node}=[" + Argument[_+1] +",draw]"
        count_nodestyle += 1
        if count_nodestyle > 1:
            print('Incorrect invocation')
            error = 1
            break
    if Argument[_][0] == '-':
        if Argument[_] not in valid:
            print('Incorrect invocation')
            error = 1
            break
if error != 1:
    if filename == '':
        print('Incorrect invocation')
        error = 1
    if Argument[len(Argument)-1].split('.')[1] != 'txt':
        print('Incorrect invocation')
        error = 1
    # print('this is the filename:',filename)
    count_line = 0
    valid_line = []
    if os.path.isfile(filename) == False:
        print('No file named {} in current directory'.format(filename))
        error = 1
    if error != 1:
        with open(filename, 'r', encoding= "utf-8") as file:
            for line in file:
                if line.strip():
                    # print(line,end='')
                    valid_line.append(line)
                    count_line += 1
                    if '\t' in line:
                        print('Incorrect invocation')
                        error = 1
        if count_line < 2:
            print('Incorrect invocation')
            error = 1
        # print(valid_line)
        # for _ in range(len(valid_line)):
        #     print(valid_line[_], len(valid_line[_]) - len(valid_line[_].lstrip(' ')))
        # print('-----------------------')
        if error != 1:
            x = len(valid_line[0]) - len(valid_line[0].lstrip(' '))
            y = len(valid_line[1]) - len(valid_line[1].lstrip(' ')) - x
            n = []
            count_lead_node = 0
            for _ in range(len(valid_line)):
                # print('Step {}'.format(_))
                if y == 0:
                    print('Wrong number of leading spaces on nonblank line {}'.format(_+2))
                    error = 1
                    break
                n.append((len(valid_line[_]) - len(valid_line[_].lstrip(' ')) - x ) // y)
                if ((len(valid_line[_]) - len(valid_line[_].lstrip(' ')) - x ) % y ) != 0 or n[_] < 0:
                    print('Wrong number of leading spaces on nonblank line {}'.format(_+1))
                    error = 1
                    break
                if  n[_] > n[_-1]+1:
                    print('Wrong number of leading spaces on nonblank line {}'.format(_+1))
                    error = 1
                    break
                if n[_] == 0:
                    count_lead_node += 1
                    if count_lead_node > 1:
                        print('Wrong number of leading spaces on nonblank line {}'.format(_+1))
                        error = 1
                        break
                # print(n[_], valid_line[_], end = '')
                valid_line[_] = (valid_line[_].replace('\n','')).strip()
            if error  != 1:
            # print(n,len(n),valid_line,len(valid_line))
                level = 0
                new_filename = filename.replace(".txt","")
                with open(new_filename +'.tex', 'w') as new_file:
                    print('\documentclass[10pt]{article}', file=new_file)
                    print('\\usepackage{tikz}', file=new_file)
                    print('\\usetikzlibrary{shapes}', file=new_file)
                    print('\pagestyle{empty}\n',file=new_file)
                    print('\\begin{document}\n',file=new_file)
                    print('\\begin{center}',file=new_file)
                    print('\\begin{tikzpicture}',file=new_file)
                    if grow != '':
                        print(grow,file=new_file)
                    if nodestyle != '':
                        print(nodestyle,file=new_file)
                    print('\\', end='',file =  new_file)
                    for _ in range(len(n)):
                        if _ > 0 :
                            print('',file =  new_file)
                            print('    ' * n[_], end='',file =  new_file)
                        if valid_line[_] == '\x0e':
                            if n[_+1] <= n[_]:
                                print('child',file =  new_file,end='')
                            else:
                                print('child {',file =  new_file,end='')
                            if _ < len(n)-2:
                                if n[_] > n[_+1]:
                                    print('',file =  new_file)
                        if valid_line[_] == '\x05':
                            print('child[fill=none] {edge from parent[draw=none]}',file =  new_file, end = '')
                            if _ < len(n)-2:
                                if n[_] > n[_+1]:
                                    print('',file =  new_file)
                        if valid_line[_] != '\x05' and valid_line[_] != '\x0e':
                            if _ > 0 :
                                print('child {', end='',file =  new_file)
                            print('node ' + '{' + valid_line[_] + '}', end='',file =  new_file)
                        if _ > 0:
                            if _+1 < len(n):
                                if n[_] >= n[_+1]:
                                    edit = 0
                                    if valid_line[_] != '\x05' and valid_line[_] != '\x0e':
                                        edit = 0
                                    else:
                                        edit = 1
                                    count_brac = 0
                                    for i in range(n[_] - n[_+1]+1- edit):
                                        if i > 0 - edit:
                                            print('    ' * ((n[_]- i)- edit), end='',file =  new_file)
                                        print('}', end = '',file =  new_file)
                                        if i != (n[_] - n[_+1]-edit):
                                            print('',file =  new_file)
                            else:
                                for i in range(n[_]):
                                    if i > 0:
                                        print('    '* (n[_]- i- edit), end = '',file =  new_file)
                                    print('}', end = '',file =  new_file)

                                    if i != n[_] - 1:
                                        print('',file = new_file)
                    print(';',file =  new_file)


                    print('\end{tikzpicture}',file =  new_file)
                    print('\end{center}\n',file =  new_file)
                    print('\end{document}',file =  new_file)