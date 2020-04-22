from textwrap import indent, dedent

from node import Node


class MOBI(Node):
    name = "MOBI"

    def __init__(self, id):
        super().__init__(id)

        self.battery = Battery()
        self.separation_detected = False
        self.battery_switch_opened = True
        self.CV_in = CV()
        self.CV_out = CV()
        self.bus = Bus()

    def __str__(self):
        text = f"""MOBI #{self.id}
    State:
        Separation detected: {self.separation_detected}
        Battery switch state: {'Opened' if self.battery_switch_opened else 'Closed'}
    Bus:
{indent(str(self.bus), 8 * " ")}
    CVs:
        CV_in:
{indent(str(self.CV_in), 12 * " ")}
        CV_out:
{indent(str(self.CV_out), 12 * " ")}
    Battery:
{indent(str(self.battery), 8 * " ")}
    CAN:
{indent(str(self.CAN), 8 * " ")}
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
        Vset: {self.Vset}V
        Iset: {self.Iset}A
        Iout: {self.Iout}A
        Temperature: {self.temperature}°C\
        """

        return dedent(text)


class Bus:
    def __init__(self):
        self.current = 0
        self.voltage = 0

    def __str__(self) -> str:
        text = f"""\
        Voltage: {self.voltage}V
        Current: {self.current}A\
        """

        return dedent(text)


class Battery:
    def __init__(self, P: int = 10):
        # Battery configuration
        self.S = 12  # For our demonstrator, S is always 12
        self.P = P
        self.cells = [Cell() for _ in range(self.P)]

        # Battery State
        self.voltage = 0
        self.current = 0
        self.SOC = 0
        self.SOH = 0

    def __str__(self):
        """ String representation of the battery"""

        text = f"""\
        Configuration: {self.S}S{self.P}P
        Voltage: {self.voltage}V 
        Current: {self.current}A
        Cells details:
        """

        text = dedent(text)
        for p, cell in enumerate(self.cells):
            text += f"    Cell #{p}: {cell}"
            if p != len(self.cells) - 1:
                text += "\n"

        return text


class Cell:
    def __init__(self, voltage: int = 0):
        self.voltage = voltage
        self.temperature = 0

    def __str__(self) -> str:
        return f"{self.voltage}V / {self.temperature}°C"


if __name__ == "__main__":
    MOBI_1 = MOBI(1)

    print(MOBI_1)

    MOBI_1.CV_out.Iout = 12

    print(MOBI_1)
