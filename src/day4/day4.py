from utils.utils import getLinesOfFile


class Pair:
    def __init__(self, row:str):
        pair = row.split(',')
        self.first = (int(pair[0].split('-')[0]), int(pair[0].split('-')[1]))
        self.second = (int(pair[1].split('-')[0]), int(pair[1].split('-')[1]))

    def isOneContainedInTheOther(self):
        if self.first[0] in range(self.second[0],self.second[1]+1) and self.first[1] in range(self.second[0],self.second[1]+1):
            return True
        elif self.second[0] in range(self.first[0],self.first[1]+1) and self.second[1] in range(self.first[0],self.first[1]+1):
            return True
        else:
            return False

    def isPartiallyContainedInTheOther(self):
        if self.first[0] in range(self.second[0],self.second[1]+1) or self.first[1] in range(self.second[0],self.second[1]+1):
            return True
        elif self.second[0] in range(self.first[0],self.first[1]+1) or self.second[1] in range(self.first[0],self.first[1]+1):
            return True
        else:
            return False

if __name__ == '__main__':
    pairs = [Pair(elem) for elem in getLinesOfFile('input.txt')]
    count = 0
    for pair in pairs:
        if pair.isOneContainedInTheOther():
            count += 1
    print(f"{count} elves have entirely overlapping fields")

    count2 = 0
    for pair in pairs:
        if pair.isPartiallyContainedInTheOther():
            count2 += 1
    print(f"{count2} elves have partially overlapping fields")