from textwrap import dedent


class Node:
    def __init__(self, id):
        self.id = id
        self.reset_count = 0
        self.CAN = CAN()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}#{self.id}"


class CAN:
    def __init__(self):
        self.TEC = 0
        self.REC = 0

    def __str__(self) -> str:
        text = f"""\
        TEC: {self.TEC}
        REC: {self.REC}\
        """

        return dedent(text)
