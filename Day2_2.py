inputPath = r"C:\Users\js18511\Downloads\Day2.txt"

example = '''A Y
B X
C Z'''


def readFile(path):
    File = open(str(path))
    FileContent = File.read()
    return FileContent

def convertStr(inputstr):
    outputstr = inputstr.replace('X', 'Loose')
    outputstr = outputstr.replace('Y', 'Draw')
    outputstr = outputstr.replace('Z', 'Win')
    outputstr = outputstr.replace('A', 'Rock')
    outputstr = outputstr.replace('B', 'Paper')
    outputstr = outputstr.replace('C', 'Scissors')
    outputlist = outputstr.split('\n')

    return outputlist

def neededPick(pickList):
    RPSdict = {'Loose':{'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'},
     'Win':{'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'},
               'Draw': {'Rock': 'Rock', 'Paper': 'Paper', 'Scissors': 'Scissors'}
        }
    return RPSdict[pickList[1]][pickList[0]]

def CalcRound(picks):
    me = neededPick(picks)
    opponent = picks[0]
    points = 0
    if me == 'Rock':
        points += 1
        if opponent == 'Scissors':
            points += 6
    if me == 'Paper':
        points += 2
        if opponent == 'Rock':
            points += 6
    if me == 'Scissors':
        points += 3
        if opponent == 'Paper':
            points += 6
    if me == opponent:
        points += 3
    return points


resultpoints = 0
pairslist = convertStr(readFile(inputPath))
for pairs in pairslist:
    roundpoints = CalcRound(pairs.split())
    resultpoints += roundpoints
print(resultpoints)
