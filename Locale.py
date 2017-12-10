class Locale:
    def __init__(self, name, longDes, shortDes, wasVisited, wasSearched, items):
        self.name = name
        self.longDes = longDes
        self.shortDes = shortDes
        self.wasVisited = wasVisited
        self.wasSearched = wasSearched
        self.items = items

    def printLong(self):
        print(self.longDes)

    def printShort(self):
        print(self.shortDes)

    def visitLoc(self):
        self.wasVisited = True

    def searchLoc(self):
        self.wasSearched = True

    def remItem(self):
        self.items = "nothing"
