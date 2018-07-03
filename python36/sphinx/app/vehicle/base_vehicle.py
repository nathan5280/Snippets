from abc import ABC


class BaseVehicle(ABC):
    """
    Base Vehicle provides common functionality about different types of vehicles.


    :param common_name: Common name for the vehicle (car, truck, motorcycle, ...)
    :param num_wheels: Number of wheels on the vehicle.
    :param engine_displacement: Engine displacement for the vehicle (cubic inches.)
    """

    def __init__(self, *, common_name: str, num_wheels: int, engine_displacement: int):
        """
        Initialize a base vehicle.
        """
        self.common_name = common_name
        self.num_wheels = num_wheels
        self.engine_displacement = engine_displacement

    def __repr__(self) -> str:
        """
        Simple text description of the vehicle.

        :return: Text representation
        """

        return f"<name={self.common_name}, wheels={self.num_wheels}, displacement={self.engine_displacement}>"

    def common_name(self) -> str:
        """
        Get the common name for the vehicle.

        :return:
        """

        return self.common_name
