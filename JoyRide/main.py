# CODE CELL
#
# Write the park function so that it actually parks your vehicle.
# Use Car.gas() to set the acceleration.
# Rememeber v = at and x = vt + 1/2at^2
# You will not need these equations but just
# to inform your intuition

from Car import Car
import time


def park(car):
    # TODO: Fix this function!
    #  currently it just drives back and forth
    #  Note that the allowed steering angles are
    #  between -25.0 and 25.0 degrees and the
    #  allowed values for gas are between -1.0 and 1.0

    # back up for 3 seconds
    car.steer(25.0)
    car.gas(-0.5)
    time.sleep(3.0)  # note how time.sleep works

    # back again...
    car.steer(-25.0)
    car.gas(-0.25)
    time.sleep(3.0)

    # forward...
    car.steer(0.0)
    car.gas(0.2)
    time.sleep(1.0)
    car.gas(-0.05)

    # Stop
    time.sleep(1.0)
    car.gas(0.0)


car = Car()
park(car)