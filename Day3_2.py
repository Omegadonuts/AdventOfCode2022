import string

example = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

Inputpath = r"C:\Users\jan\Downloads\Day3.txt"

def readFile(path):
    File = open(str(path))
    FileContent = File.read()
    return FileContent

example = readFile(Inputpath)

rucksackList = example.splitlines()

dictMap = {}
asciiletters = list(string.ascii_letters)
for i in range(len(asciiletters)):
    dictMap[asciiletters[i]] = i+1
priorityDict = dictMap

overallvalue = 0
for groupnumber in range(1, int(len(rucksackList)/3)+1):
    currentgroup = (rucksackList[(groupnumber-1) * 3:groupnumber*3])
    print(currentgroup)
    for letters in currentgroup[0]:
        if currentgroup[1].find(letters) != -1 and currentgroup[2].find(letters) != -1:
            currentValue = priorityDict[letters]
    overallvalue +=currentValue

print(overallvalue)



