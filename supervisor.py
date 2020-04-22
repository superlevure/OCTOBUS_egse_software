class MotherSupervisor:
    """Mother of all supervisors

    You don't need to mess with this
    """

    def __init__(self, name: str):
        self.name = name
        self.BOMO_loaded = False
        self.MOBI_loaded = False

    def load_BOMO(self, BOMOs: list):
        assert isinstance(BOMOs, list), "BOMOs argument must be a *list* of BOMOs"

        self.BOMOs = BOMOs
        print(self.BOMOs)

        self.BOMO_loaded = True

    def load_MOBI(self, MOBIs: list):
        assert isinstance(MOBIs, list), "MOBIs argument must be a *list* of MOBIs"

        self.MOBIs = MOBIs

        self.MOBI_loaded = True


class Supervisor(MotherSupervisor):
    """A custom supervisor

    This is the class that you would write Quentin for each of yours supervisors
    """

    def run(self):
        """ Example for a run method. """

        if not (self.BOMO_loaded or self.MOBI_loaded):
            print("You must load at least one BOMO or MOBI to run supervisor.")
        else:
            print("running supervisor..")
            print("MOBIs battery's voltage:")
            for MOBI in self.MOBIs:
                print(f"\tMOBI #{MOBI.id}: {MOBI.battery.voltage}V")


if __name__ == "__main__":

    """Usage example"""

    from MOBI import MOBI

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

    # Ok this time let's create another pair of MOBIs and add them to the supervisor
    # Note that it will replace the precedent MOBI(s) loaded
    MOBIs = [MOBI(1), MOBI(2)]
    supervisor.load_MOBI(MOBIs)
    supervisor.run()
    print("")
