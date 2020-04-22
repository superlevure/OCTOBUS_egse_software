from node import Node


class BOMO(Node):
    def __init__(self, id):
        super().__init__(id)

    def __str__(self) -> str:
        text = f"""BOMO #{self.id}"""

        return text
