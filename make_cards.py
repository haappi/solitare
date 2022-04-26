import os
import typing

number_mappings: typing.Final = {
    "ace": "ace",
    "1": "ace",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "jack": "jack",
    "queen": "queen",
    "king": "king",
}


def get_if_file_exists(file_name) -> bool:
    return os.path.isfile("./Cards/CardObjects/" + file_name + ".py")


def create_file(file_name, class_name: str = ""):
    if class_name == "":
        holder = file_name.removesuffix(".py").split("_")
        for i in holder:
            class_name += i.capitalize()
    _file = open("./Cards/CardObjects/" + file_name + ".py", "w")
    content = f"from Cards import CardObjects\n" \
        f"from utils import Card\n" \
        f"\n" \
        f"class {class_name}(Card):\n" \
        f"    def __init__(self):\n" \
        f"        super().__init__(**CardObjects.get_types(__file__))\n" \
        f"\n" \
        f"    def __new__(cls, *args, **kwargs):\n" \
        f"        return super().__new__(cls, *args, **kwargs)\n"
    _file.write(content)
    _file.close()
    return None


def get_file_formatting(asset_name: str) -> typing.Union[str, None]:
    name = asset_name.removesuffix(".png").split("_")
    if len(name) != 3:
        return None
    return f"{number_mappings[name[0]]}_{name[1]}_{name[2]}.py"


def main():
    for _file in os.listdir("./assets/cards"):
        if os.path.isfile(os.path.join("./assets/cards", _file)):
            if _file.endswith(".png"):
                formatting = get_file_formatting(_file)
                if formatting is None: continue
                if get_if_file_exists(formatting): continue
                create_file(formatting)
                print(f"Created {formatting}")
