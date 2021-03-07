def get_data():
    file = open("data.in", "r")
    data = [int(entry) for entry in file.read().split("\n")]
    file.close()

    return data


def _multiply_numbers(numbers):
    result = 1

    for number in numbers:
        result *= number

    return result


def _subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1 :]
        yield from _subset_sum(remaining, target, partial + [n], partial_sum + n)


def _get_results(data):
    return sorted(
        [
            _multiply_numbers(resulting_entries)
            for resulting_entries in list(_subset_sum(data, 2020))
        ]
    )


def get_product_of_two_entries_that_sum_to_2020(data):
    return _get_results(data)[0]


def get_product_of_three_entries_that_sum_to_2020(data):
    return _get_results(data)[1]
