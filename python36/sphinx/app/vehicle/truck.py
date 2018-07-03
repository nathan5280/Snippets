from vehicle.base_vehicle import BaseVehicle


class Truck(BaseVehicle):
    """
    Truck specialization of BaseVehicle

    :param num_wheels: Number of wheels on the vehicle.
    :param engine_displacement: Engine displacement for the vehicle (cubic inches.)
    :param dump: Indicates of the truck has a dump body.
    """

    def __init__(self, *, num_wheels: int, engine_displacement: int, dump: bool = False):
        """
        Initialize a truck vehicle.
        """

        super().__init__(common_name="Truck", num_wheels=num_wheels, engine_displacement=engine_displacement)

        self.dump = dump

    def is_dump(self) -> bool:
        """
        Check if the truck has a dump body.

        :return: True if dump body.
        """

        return self.dump
