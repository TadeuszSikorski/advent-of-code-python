def get_data():
    file = open("data.in", "r")
    data = file.read()
    file.close()

    return data


def create_floors(brackets):
    floor = 0
    floors = []

    for bracket in brackets:
        if bracket == "(":
            floor += 1
            floors.append(floor)
        if bracket == ")":
            floor -= 1
            floors.append(floor)
    return floors


def check_position(floors, floor):
    return floors.index(floor) + 1
