from utils.utils import getLinesOfFile

class Game:
    def __init__(self):
        self.rows = [['N', 'B', 'D', 'T', 'V', 'G', 'Z', 'J'],
                     ['S', 'R', 'M', 'D', 'W', 'P', 'F'],
                     ['V', 'C', 'R', 'S', 'Z'],
                     ['R', 'T', 'J', 'Z', 'P', 'H', 'G'],
                     ['T', 'C', 'J', 'N', 'D', 'Z', 'Q', 'F'],
                     ['N', 'V', 'P', 'W', 'G', 'S', 'F', 'M'],
                     ['G', 'C', 'V', 'B', 'P', 'Q'],
                     ['Z', 'B', 'P', 'N'],
                     ['W', 'P', 'J']]

    def move(self, move: str, crane="CraneMover9000"):
        split = move.split(' ')
        piecesToMove = int(split[1])
        startingColumn = int(split[3])-1
        endingColumn = int(split[5])-1
        numOfPiecesInColumn = len(self.rows[startingColumn])
        piecesToBeMoved = self.rows[startingColumn][numOfPiecesInColumn-piecesToMove:numOfPiecesInColumn]
        if crane != "CraneMover9001":
            piecesToBeMoved.reverse()
        self.rows[startingColumn] = self.rows[startingColumn][:numOfPiecesInColumn-len(piecesToBeMoved)]
        self.rows[endingColumn].extend(piecesToBeMoved)

    def topLetters(self):
        for row in self.rows:
            print(row[len(row)-1], end='')

if __name__ == '__main__':
    moves = getLinesOfFile('input.txt')
    game1 = Game()
    for move in moves:
        game1.move(move)

    print('CraneMover 9000 top crates')
    game1.topLetters()
    print()

    game2 = Game()
    for move in moves:
        game2.move(move, crane="CraneMover9001")

    print('CraneMover 9001 top crates')
    game2.topLetters()
    print()