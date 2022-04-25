import os
import typing

name_mappings: typing.Final = {
    "hearts": "heart",
    "diamonds": "diamond",
    "spades": "spade",
    "clubs": "club"
}

number_mappings: typing.Final = {
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
}

color_mappings: typing.Final = {
    "heart": "red",
    "club": "black",
    "diamond": "red",
    "spade": "black"
}


def get_types(filename: str) -> dict:
    """
    Returns a dict with the type of the card based on the file name

    Pass __file__, and this function will do the rest for you.
    :param filename: A string
    :return: A dict containing the values of the card which can be passed as a **kwargs to the Card class
    """
    __filename: str = os.path.basename(filename).split(".")[0]
    __parts: typing.List[str] = __filename.split("_")
    return {
        "number": number_mappings[int(__parts[0])],
        "suite": name_mappings[__parts[2]],
        "color": color_mappings[name_mappings[__parts[2]]]
    }
