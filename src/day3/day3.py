from utils.utils import getLinesOfFile

def getPriority(char: str):
    asciiVal = ord(char[0])
    if(asciiVal>=97 and asciiVal<=122):
        # lettera minuscola
        return asciiVal-96
    else:
        #lettera maiuscola
        return asciiVal - 65 + 27

def findLetterInBothString(s1,s2):
    for char in s1:
        if char in s2:
            return char
    return "ERROR"

def findLetterInAllString(s1,s2,s3):
    for char in s1:
        if char in s2 and char in s3:
            return char
    return "ERROR"
class Rucksack:
    def __init__(self, row:str):
        self.rucksack = row
        self.firstCompartment = row[:len(row)//2]
        self.secondCompartment = row[len(row)//2:]

if __name__ == '__main__':
    rucksacks = [Rucksack(elem) for elem in getLinesOfFile('input.txt')]
    priorities = [getPriority(findLetterInBothString(elem.firstCompartment, elem.secondCompartment)) for elem in rucksacks]
    print(f"sum of priorities is {sum(priorities)}")

    groups = [getLinesOfFile('input.txt')[n:n+3] for n in range(0, len(rucksacks), 3)]
    priorities2 = [getPriority(findLetterInAllString(*group)) for group in groups]
    print(f"sum of priorities of badges is {sum(priorities2)}")


