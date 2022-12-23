# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List


class Elf:
    def __init__(self, calories: List[str]):
        self.carriedCalories = calories.copy()

    def totalCalories(self):
        return sum([int(cal) for cal in self.carriedCalories])


def getLinesOfFile(filename: str):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def getElvesFromFile():
    lines = getLinesOfFile('src/day1/input.txt')
    tmp = []
    elves = []
    for line in lines:
        if line == "":
            elves.append(Elf(tmp))
            tmp.clear()
        else:
            tmp.append(line)
    return elves


def getMaxCalories(elves: List[Elf], n=1):
    return sorted([elf.totalCalories() for elf in elves], reverse=True)[0:n]


if __name__ == '__main__':
    elves = getElvesFromFile()
    print(f"elf carrying max calories is carrying {getMaxCalories(elves)}")
    print(f"top 3 carrying calories are carrying {getMaxCalories(elves,3)} sum is {sum(getMaxCalories(elves,3))}")
