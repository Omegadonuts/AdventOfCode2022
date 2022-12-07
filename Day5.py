example = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

stacks = example.split('\n\n')[0]
proc = example.split('\n\n')[1]

tasks = []
for task in proc.splitlines():
    moveval = task.split(' ')[1]
    fromval = task.split(' ')[3]
    toval = task.split(' ')[5]
    tasks.append([moveval, fromval, toval])

splitstacks = stacks.split('\n')
for i in range(len(splitstacks)):
    splitstacks[i] = splitstacks[i].replace('    ', '[x]')
    splitstacks[i] = splitstacks[i].replace(' ', '')
    splitstacks[i] = splitstacks[i].replace('[', '')
    splitstacks[i] = splitstacks[i].replace(']', '')

columns = int(splitstacks[-1][-1])
columnslist = ['', '', '', '', '', '', '', '', '']
columnslistp2 = []

splitstacks.pop(-1)

for n in range(columns):
    for row in splitstacks:
        columnslist[n] = columnslist[n] + row[n]
        columnslist[n] = columnslist[n].replace('x','')
        #columnslistp2[n] = columnslistp2[n] + row[n]
        #columnslistp2[n] = columnslistp2[n].replace('x','')        
columnslistp2.extend(columnslist)

for task in tasks:
    moveval = int(task[0])
    fromval = int(task[1])-1
    toval = int(task[2])-1
    moveblock = columnslist[fromval][0:(moveval)]
    columnslist[fromval] = columnslist[fromval][moveval:]
    columnslist[toval] = moveblock[::-1] + columnslist[toval]
    moveblockp2 = columnslistp2[fromval][0:(moveval)]
    columnslistp2[fromval] = columnslistp2[fromval][moveval:]
    columnslistp2[toval] = moveblockp2 + columnslistp2[toval]
    
result = ''
resultp2=''

for column in columnslist:
    if len(column)>0:
        result += column[0]
        
for column in columnslistp2:
    if len(column)>0:
        resultp2 += column[0]
print('Result Part1: '+ result)
print('Result Part2: '+ resultp2)
