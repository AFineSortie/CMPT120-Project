class Player:
    def __init__(self, name, score, nameLoc, numLoc, moveCount, inventory):
        self.name = name
        self.score = score
        self.nameLoc = nameLoc
        self.numLoc = numLoc
        self.moveCount = moveCount
        self.inventory = inventory

    def addScore(self):
        self.score = self.score + 5

    def dropItem(self, item):
        self.inventory.remove(item)

    def remItem(self, item):
        self.inventory.remove(item)
