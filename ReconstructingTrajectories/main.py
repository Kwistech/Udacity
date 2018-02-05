from math import sin, cos, tan, pi
from matplotlib import pyplot as plt


def get_speeds(data_list):  # Done
    """returns a length N list where entry i contains the speed (m/s) of the
    vehicle at t=i×Δt."""
    times = [data[0] for data in data_list]
    displacements = [data[1] for data in data_list]

    prev_time = times[0]
    prev_displacement = displacements[0]

    speeds = [0, ]

    for i in range(1, len(data_list)):
        time = times[i]
        displacement = displacements[i]

        delta_t = time - prev_time
        delta_d = displacement - prev_displacement

        speed = delta_d / delta_t
        speeds.append(speed)

        prev_time = time
        prev_displacement = displacement

    return speeds


def get_headings(data_list):  # Done
    """returns a length N list where entry i contains the heading (radians,
    0≤θ<2π) of the vehicle at t=i×Δt."""
    times = [data[0] for data in data_list]
    yaw_rates = [data[2] for data in data_list]

    prev_time = times[0]

    headings_sum = 0
    headings = [0, ]

    for i in range(1, len(data_list)):
        time = times[i]
        yaw = yaw_rates[i]

        delta_t = time - prev_time

        heading = delta_t * yaw
        headings_sum += heading
        headings.append(headings_sum)

        prev_time = time
        prev_yaw = yaw

    return headings


def get_x_y(data_list):
    """returns a length N list where entry i contains an (x, y) tuple
    corresponding to the x and y
    coordinates (meters) of the vehicle at t=i×Δt."""
    displacements = [data[1] for data in data_list]
    headings = get_headings(data_list)

    prev_displacement = displacements[0]

    x = 0
    y = 0

    x_y = [(0, 0), ]

    for i in range(1, len(data_list)):
        displacement = displacements[i]
        angle = headings[i]

        delta_d = displacement - prev_displacement

        delta_x = cos(angle) * delta_d
        delta_y = sin(angle) * delta_d

        new_x = x + delta_x
        new_y = y + delta_y

        x_y.append((x, y))

        x = new_x
        y = new_y

        prev_displacement = displacement

    return x_y


def show_x_y(data_list):
    x_y_list = get_x_y(data_list)

    x_list = [data[0] for data in x_y_list]
    y_list = [data[1] for data in x_y_list]

    plt.scatter(x_list, y_list)
    plt.plot(x_list, y_list)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()