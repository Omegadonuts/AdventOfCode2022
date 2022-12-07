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
for rucksackindex in range(len(rucksackList)):
    stringlenght = len(rucksackList[rucksackindex])
    middlepos = int(stringlenght/2)
    rucksackList[rucksackindex] = [rucksackList[rucksackindex][:middlepos], rucksackList[rucksackindex][middlepos:]]

dictMap = {}
asciiletters = list(string.ascii_letters)
for i in range(len(asciiletters)):
    dictMap[asciiletters[i]] = i+1
priorityDict = dictMap

sharedItemsAllRucksacks = []
sharedRucksackValue = 0
for rucksack in rucksackList:
    compartment1 = rucksack[0]
    compartment2 = rucksack[1]
    sharedItemsCurrentRucksack = []
    for letters in compartment1:
        if compartment2.find(letters) != -1:
            if letters not in sharedItemsCurrentRucksack:
                sharedItemsCurrentRucksack.append(letters)
                currentRucksackValue = priorityDict[letters[0]]
    sharedItemsAllRucksacks.append(sharedItemsCurrentRucksack)
    sharedRucksackValue += currentRucksackValue

print(sharedRucksackValue)

