def getLinesOfFile(filename: str):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines
