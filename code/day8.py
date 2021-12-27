import collections
from util import read_input
from typing import Iterable, Mapping, Optional, Tuple, List


def parse_line() -> Tuple[List[str], List[str]]:
    """
    Get entry and output values
    """
    entry = []
    op = []
    for line in read_input("day8.txt"):
        entry.append(line.split(" | ")[0])
        op.append(line.split(" | ")[1])

    return entry, op


def unpack_number(number, map, expected_numbers2, letters_map):
    num = next(number)
    map = list(next(map))
    breakpoint()
    unpack_number(number, map)


def map_numbers(
    numbers_map: Mapping[str, int],
    expected_numbers: Mapping[str, Iterable[str]],
    letters_map: Mapping[str, Optional[str]],
):
    """
    Map the unique values to get the possible configuration
    Mapping is as follows:

        aaaa
    b           c
    b           c
        dddd
    e           f
    e           f
        gggg
    """

    # Recursively unpack the numbers
    unpack_number(iter(numbers_map.keys()), iter(numbers_map.values()), expected_numbers, letters_map)

    print(numbers_map)
    breakpoint()


def map_line_to_numbers1(
    line: str,
    unq_segments_to_number: Mapping[int, str],
    total_numbers: Mapping[str, int],
) -> List[int]:
    """
    Take one line from entry or otuput and map it to numbers based on segments.
    """
    segments = line.split(" ")
    for segment in segments:
        try:
            # 1,4,7,8 will have unique number of segments
            total_numbers[unq_segments_to_number[len(segment)]] += 1
        except KeyError:
            pass
    return total_numbers


def map_line_to_numbers2(
    line: str,
    unq_segments_to_number: Mapping[int, str],
    other_segments_to_number: Mapping[int, str],
    total_numbers2: Mapping[str, int],
    expected_numbers2: Mapping[str, Iterable[str]],
) -> List[int]:
    """
    Take one line from entry or otuput and map it to numbers based on segments.
    """
    segments = line.split(" ")
    for segment in segments:
        try:
            # 1,4,7,8 will have unique number of segments
            total_numbers2[unq_segments_to_number[len(segment)]] = segment
        except KeyError:
            # total_numbers2[str(other_segments_to_number[len(segment)])] = segment
            pass
    letters = ["a", "b", "c", "d", "e", "f", "g"]
    letters_map = dict.fromkeys(letters)
    map_numbers(total_numbers2, expected_numbers2, letters_map)
    return total_numbers2


def sum_values(total_numbers: Mapping[str, int]):
    """
    Print the sum of values
    """
    print(sum(value for value in total_numbers.values()))


def main():
    # Number of segments to number
    unq_segments_to_number = {2: "One", 4: "Four", 3: "Seven", 7: "Eight"}
    other_segments_to_number = {5: ["Two", "Three", "Five"], 6: ["Zero", "Six", "Nine"]}
    total_numbers = collections.defaultdict(int)
    total_numbers2 = collections.defaultdict(str)
    expected_numbers2 = {
        "Zero": ["a", "c", "b", "e", "f", "g"],
        "One": ["c", "f"],
        "Two": ["a", "c", "d", "e", "g"],
        "Three": ["a", "c", "d", "e", "f", "g"],
        "Four": ["b", "c", "d", "f"],
        "Five": ["a", "b", "d", "f", "g"],
        "Six": ["a", "b", "d", "e", "f", "g"],
        "Seven": ["a", "c", "f"],
        "Eight": ["a", "b", "c", "d", "e", "f", "g"],
        "Nine": ["a", "b", "c", "d", "f", "g"],
    }
    entry, op = parse_line()

    for line in op:
        total_numbers = map_line_to_numbers1(
            line, unq_segments_to_number, total_numbers
        )
    sum_values(total_numbers)

    for line in op:
        total_numbers2 = map_line_to_numbers2(
            line,
            unq_segments_to_number,
            other_segments_to_number,
            total_numbers2,
            expected_numbers2,
        )
        break


if __name__ == "__main__":
    main()
