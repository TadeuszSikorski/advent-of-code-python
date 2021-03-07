def extract_dimensions(dimensions):
    return [int(dimension) for dimension in dimensions.split("x")]


def get_data():
    file = open("data.in", "r")
    data = [extract_dimensions(dimensions) for dimensions in file.read().split("\n")]
    file.close()

    return data


def get_partial_calculations(dimensions):
    length, width, height = dimensions[0], dimensions[1], dimensions[2]

    return ((length * width), (width * height), (height * length))


def get_surface_area_of_box(dimensions):
    surface_area_of_box = 0

    for partial_calculation in get_partial_calculations(dimensions):
        surface_area_of_box += 2 * partial_calculation

    return surface_area_of_box


def get_total_of_square_feet(dimensions):
    return get_surface_area_of_box(dimensions) + min(
        get_partial_calculations(dimensions)
    )


def get_total_square_feet_of_wrapping_paper(data):
    total_square_feet_of_wrapping_paper = 0

    for dimensions in data:
        total_square_feet_of_wrapping_paper += get_total_of_square_feet(dimensions)

    return total_square_feet_of_wrapping_paper


def get_feet_of_ribbon_to_wrap_present(dimensions):
    two_dimensions = [dimension for dimension in dimensions]
    two_dimensions.remove(max(two_dimensions))

    return two_dimensions[0] + two_dimensions[0] + two_dimensions[1] + two_dimensions[1]


def get_feet_of_ribbon_for_bow(dimensions):
    feet_of_ribbon_for_bow = 1

    for dimension in dimensions:
        feet_of_ribbon_for_bow *= dimension

    return feet_of_ribbon_for_bow


def get_total_of_feet(dimensions):
    return get_feet_of_ribbon_to_wrap_present(dimensions) + get_feet_of_ribbon_for_bow(
        dimensions
    )


def get_total_feet_of_ribbon(data):
    total_feet_of_ribbon = 0

    for dimensions in data:
        total_feet_of_ribbon += get_total_of_feet(dimensions)

    return total_feet_of_ribbon
