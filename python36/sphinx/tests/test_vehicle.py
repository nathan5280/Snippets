from vehicle.truck import Truck


def test_truck_no_dump():
    # given
    # execute
    truck = Truck(num_wheels=4, engine_displacement=380)

    # expect
    assert "<name=Truck, wheels=4, displacement=380>" == str(truck)
    assert not truck.is_dump()