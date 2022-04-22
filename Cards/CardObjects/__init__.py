import os
import typing

name_mappings: typing.Final = {
    "hearts": "heart",
    "diamonds": "diamond",
    "spades": "spade",
    "clubs": "club"
}

color_mappings: typing.Final = {
    "heart": "red",
    "club": "black",
    "diamond": "red",
    "spade": "black"
}


def get_types(filename: str) -> dict:
    """
    Returns a tuple with the type of the card based on the file name

    Pass __file__, and this function will do the rest for you.
    :param filename: A string
    :return:
    """
    __filename: str = os.path.basename(filename).split(".")[0]
    __parts: typing.List[str] = __filename.split("_")
    print(__parts)
    # return {
    #     "suite": __parts[0],
    #     "number": __parts[1],
    # }  # todo return a dict -> pass as kwargs into CardObject init function
    return int(__parts[0]), name_mappings[__parts[2]], color_mappings[name_mappings[__parts[2]]]

