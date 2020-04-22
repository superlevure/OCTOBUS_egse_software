from textwrap import dedent


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
            text += f"\tCell [{p}]: {cell.voltage}V / {cell.temperature}°C\n"

        return text


class Cell:
    def __init__(self, voltage: int = 0):
        self.voltage = 0
        self.temperature = 0


if __name__ == "__main__":
    battery = Battery()

    print(battery)
