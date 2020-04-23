class MotherSupervisor:
    """Mother of all supervisors

    You don't need to mess with this

    Attributes:
        name (str)
        BOMOs (list): List of BOMO(s)
        MOBIs (list): List of MOBI(s)
    """

    def __init__(self, name: str):
        self.name = name
        self.BOMOs = []
        self.MOBIs = []

    def load_BOMO(self, BOMOs: list):
        """Loads BOMO(s) into the supervisor

        Arguments:
            BOMOs (list): List of BOMO(s)
        """
        assert isinstance(BOMOs, list), "BOMOs argument must be a *list* of BOMOs"

        self.BOMOs = BOMOs

    def load_MOBI(self, MOBIs: list):
        """Loads MOBI(s) into the supervisor

        Arguments:
            MOBIs (list): List of MOBI(s)
        """
        assert isinstance(MOBIs, list), "MOBIs argument must be a *list* of MOBIs"

        self.MOBIs = MOBIs


class Supervisor(MotherSupervisor):
    """A custom supervisor

    This is the class that you would write Quentin for each of your supervisors
    """

    def run(self):
        """ Example for a run method. """

        if len(self.BOMOs) == 0 and len(self.MOBIs) == 0:
            print("You must load at least one BOMO or MOBI to run supervisor.")
        else:
            print("running supervisor..")

            print(f"Setup:")

            print(f"{len(self.MOBIs)} MOBI(s) loaded")
            print(f"{len(self.BOMOs)} BOMO(s) loaded")

            print("MOBIs battery's voltage:")
            for MOBI in self.MOBIs:
                print(f"\tMOBI #{MOBI.id}: {MOBI.battery.voltage}V")


if __name__ == "__main__":

    """Usage example"""

    from MOBI import MOBI
    from BOMO import BOMO

    # Let's create a MOBI
    MOBI_1 = MOBI(1)

    # Then a custom supervisor
    supervisor = Supervisor(name="Test")

    # We load the MOBI into our supervisor (you only need to do this once)
    supervisor.load_MOBI([MOBI_1])

    # Then we run the supervisor main algorythm
    supervisor.run()
    print("")
    # Let's update the voltage of our MOBI's battery
    MOBI_1.battery.voltage = 10

    # If we run the supervisor's algorythm again, it will use our updated battery voltage
    supervisor.run()
    print("")

    # Ok this time let's create another pair of MOBIs and BOMOs and add them to the supervisor
    # Note that it will replace the precedent MOBI(s) loaded
    MOBIs = [MOBI(1), MOBI(2)]
    BOMOs = [BOMO(1), BOMO(2), BOMO(3)]

    supervisor.load_MOBI(MOBIs)
    supervisor.load_BOMO(BOMOs)
    supervisor.run()
    print("")

    # One can access any node's information easily
    print("MOBI #0 - CV in - Iout = ", end="")
    print(MOBIs[0].CV_in.Iout, end="")
    print("A")

    MOBIs[0].CV_in.Iout = 23

    print("MOBI #0 - CV in - Iout = ", end="")
    print(MOBIs[0].CV_in.Iout, end="")
    print("A")
