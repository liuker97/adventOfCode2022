from utils.utils import getLinesOfFile

opponentMoveDict = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissor',
}
pointsDict = {
    'loss': 0,
    'win': 6,
    'draw': 3,
    'rock': 1,
    'paper': 2,
    'scissor': 3,
}

winners = {
    'rock':'scissor',
    'scissor':'paper',
    'paper':'rock',
}
loosers = {
    'scissor': 'rock',
    'paper': 'scissor',
    'rock': 'paper'
}
strategy1 = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissor',
}
strategy2 = {
    'X': 'loss',
    'Y': 'draw',
    'Z': 'win',
}

def getScore(me, opponent):
    if me == opponent:
        return pointsDict['draw'] + pointsDict[me]
    if winners[me] == opponent:
        return pointsDict['win'] + pointsDict[me]
    else:
        return pointsDict['loss'] + pointsDict[me]

def getScoreStrategy2(me,opponent):
    if strategy2[me] == 'draw':
        picked = opponent
    elif strategy2[me] == 'win':
        picked = loosers[opponent]
    else:
        picked = winners[opponent]

    return getScore(picked, opponent)

def getScoreStrategy1(me,opponent):
    picked = strategy1[me]
    return getScore(picked,opponent)


class GameRound:
    def __init__(self, fileRow: str):
        round = fileRow.split(' ')
        self.opponent = opponentMoveDict[round[0]]
        self.me = round[1]



if __name__ == '__main__':
    rows = getLinesOfFile('input.txt')
    rounds = []
    for row in rows:
        rounds.append(GameRound(row))
    print(f"Following the strategy you would get {sum(getScoreStrategy1(round.me,round.opponent) for round in rounds)} points")
    print(f"Following the strategy2 you would get {sum(getScoreStrategy2(round.me,round.opponent) for round in rounds)} points")
