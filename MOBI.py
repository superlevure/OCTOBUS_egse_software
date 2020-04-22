from textwrap import indent, dedent

from node import Node
from battery import Battery


class MOBI(Node):
    name = "MOBI"

    def __init__(self, id):
        super().__init__(id)

        self.battery = Battery()
        self.separation_detected = False
        self.CV_in = CV()
        self.CV_out = CV()

    # This attribute Ibus comes from the CV_out so we
    # use a getter and a setter to access it
    @property
    def Ibus(self):
        return self.CV_out.Iout

    @Ibus.setter
    def Ibus(self, value):
        self.CV_out.Iout = value

    def __str__(self):
        text = f"""MOBI #{self.id}
    State:
        Separation detected: {self.separation_detected}
        Bus current (Ibus): {self.Ibus}A
    CVs:
        CV_in:
{indent(str(self.CV_in), 12 * " ")}
        CV_out:
{indent(str(self.CV_out), 12 * " ")}
    Battery:
{indent(str(self.battery), 8 * " ")}
        """
        return text


class CV:
    def __init__(self):
        self.Iset = 0
        self.Vset = 0
        self.state = "OFF"
        self.temperature = 0
        self.Iout = 0

    def __str__(self) -> str:
        text = f"""\
        State {self.state}
        Iset: {self.Iset}
        Vset: {self.Vset}
        Iout: {self.Iout}
        Temperature: {self.temperature}\
        """

        return dedent(text)


if __name__ == "__main__":
    MOBI_1 = MOBI(1)

    print(MOBI_1)

    MOBI_1.CV_out.Iout = 12

    print(MOBI_1)
