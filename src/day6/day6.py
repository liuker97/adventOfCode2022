from utils.utils import getLinesOfFile


def allUnique(s: str):
    unique = True
    for i in range(0, len(s) - 1):
        if s[i] in s[i + 1:]:
            unique = False
            break
    return unique


def findNDifferentCharacters(code: str, n: int):
    for i in range(0, len(code) - (n - 1)):
        substr = code[i:i + n]
        if allUnique(substr):
            return substr, i + n
    return '', -1


if __name__ == '__main__':
    code = getLinesOfFile('input.txt')[0]
    first4Distinct = findNDifferentCharacters(code, 4)
    print(f"First 4 distinct characters are {first4Distinct[0]} packet starts at position {first4Distinct[1]}")
    first14Distinct = findNDifferentCharacters(code, 14)
    print(f"First 4 distinct characters are {first14Distinct[0]} message starts position {first14Distinct[1]}")
