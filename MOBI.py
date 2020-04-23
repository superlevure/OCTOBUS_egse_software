from textwrap import indent, dedent

from node import Node


class MOBI(Node):
    """MOBI class

    Attributes:
        battery (Battery): MOBI's battery
        separation_detected (bool): Strap separation detection state
        battery_switch_opened (bool): Battery's switch state
        CV_in (CV): Bus to battery convertor
        CV_out (CV): Battery to bus convertor
        bus (Bus): Bus voltage/current sensing 
        APS (APS): Auxiliary Power Supply 
    """

    name = "MOBI"

    def __init__(self, id):
        super().__init__(id)

        self.battery = Battery()
        self.separation_detected = False
        self.battery_switch_opened = True
        self.CV_in = CV()
        self.CV_out = CV()
        self.bus = Bus()
        self.APS = APS()

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
    """MOBI's CV

    Hold the state of a MOBI's CV

    Attributes: 
        Iset (float)
        Vset (float)
        state (bool): CV's state 
        temperature (float)
        Iout (float)
    """

    def __init__(self):
        self.Iset = 0.0
        self.Vset = 0.0
        self.state = "OFF"
        self.temperature = 0.0
        self.Iout = 0.0

    def __str__(self) -> str:
        text = f"""\
        State {self.state}
        Vset: {self.Vset}V
        Iset: {self.Iset}A
        Iout: {self.Iout}A
        Temperature: {self.temperature}°C\
        """

        return dedent(text)


class APS:
    """MOBI's APS

    Hold the state of a MOBI's APS

    Attributes: 
        temperature1 (float)
        temperature2 (float)
    """

    def __init__(self) -> None:
        self.temperature1 = 0.0
        self.temperature2 = 0.0


class Bus:
    """Bus sensing

    Hold the state of a MOBI's bus sensing 

    Attributes: 
        current (float)
        voltage (float)

    """

    def __init__(self):
        self.current = 0.0
        self.voltage = 0.0

    def __str__(self) -> str:
        text = f"""\
        Voltage: {self.voltage}V
        Current: {self.current}A\
        """

        return dedent(text)


class Battery:
    """MOBI's battery

    Holds the battery state of a MOBI

    Attributes:
        S (int): Number of cells in serie
        P (int): Number of strings in parallel
        cells (Cell): Battery's cells 
        voltage (float): Battery's voltage
        current (float): Battery's current
        SOC (int): Battery's State Of Charge
        SOH (int): Battery's State Of Health
        temperatures (list): BMS cells temperatures list
    """

    def __init__(self, P: int = 10):
        # Battery configuration
        self.S = 12  # For our demonstrator, S is always 12
        self.P = P
        self.cells = [Cell() for _ in range(self.P)]

        # Battery State
        self.voltage = 0.0
        self.current = 0.0
        self.SOC = 0
        self.SOH = 0
        self.temperatures = [0.0 for _ in range(5)]

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
    """Battery's Cell

    Holds the cell state of a battery

    Attributes:
        voltage (float)
    """

    def __init__(self, voltage: float = 0.0):
        self.voltage = voltage

    def __str__(self) -> str:
        return f"{self.voltage}V"


if __name__ == "__main__":
    MOBI_1 = MOBI(1)

    print(MOBI_1)

    MOBI_1.CV_out.Iout = 12

    print(MOBI_1)
