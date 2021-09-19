class Appearance:
    def __init__(self, docId, frequency, name):
        self.docId = docId
        self.frequency = frequency
        self.name = name

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        if isinstance(other, Appearance):
            return self.docId == other.docId and self.frequency == other.frequency and self.name == other.name
        return False
