class Node:
    def __init__(self, id):
        self.id = id

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}#{self.id}"
