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


def get_class_name_formatting(file_name) -> str:
    new_name = ""
    holder = file_name.removesuffix(".py").split("_")
    for i in holder:
        new_name += i.capitalize()
    return new_name


def delete_file(file_name):
    os.remove(f"./Cards/CardObjects/{file_name}")


def delete_directory_recursively():
    for _file in os.listdir("./Cards/CardObjects"):
        if _file == "__init__.py":
            continue
        delete_file(_file)

def create_file(file_name):
    class_name = get_class_name_formatting(file_name)
    _file = open("./Cards/CardObjects/" + file_name, "w")
    content = (
        f"from Cards import CardObjects\n"
        f"from utils import Card\n"
        f"\n"
        f"\n"
        f"class {class_name}(Card):\n"
        f"    def __init__(self):\n"
        f"        super().__init__(**CardObjects.get_types(__file__))\n"
        f"\n"
        f"    def __new__(cls, *args, **kwargs):\n"
        f"        return super().__new__(cls, *args, **kwargs)\n"
    )
    _file.write(content)
    _file.close()
    return None


def get_file_formatting(asset_name: str) -> typing.Union[str, None]:
    name = asset_name.removesuffix(".png").split("_")
    if len(name) != 3:
        return None
    return f"{number_mappings[name[0]]}_{name[1]}_{name[2]}.py"


def main():
    class_names = []
    file_names = []
    for _file in os.listdir("./assets/cards"):
        if os.path.isfile(os.path.join("./assets/cards", _file)):
            if _file.endswith(".png"):
                formatting = get_file_formatting(_file)
                if formatting is None:
                    print(f"{_file} is not formatted correctly")
                    continue
                class_names.append(
                    get_class_name_formatting(formatting)
                )  # I want the format to be accurate, but
                # still work if file does exist.
                file_names.append(
                    f"from Cards.CardObjects.{formatting.removesuffix('.py')} import {get_class_name_formatting(formatting)}"
                )
                if get_if_file_exists(formatting):
                    print(f"{formatting} already exists")
                    continue
                create_file(formatting)
                print(f"Created {formatting}")
    print(f"Paste the following code segment where tuples are used and import.")
    print("(" + ", ".join([s for s in class_names]) + ")")
    print("\nUse the following import statement to make your hellish life easier.\n\n")
    print("\n".join([s for s in file_names]))


main()
