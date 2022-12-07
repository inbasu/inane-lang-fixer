"""
If some one review this code:
is it bad use both word and text as parametrs for string in single class
PLEASE
"""
from capturer import *
from translator import Translator


HOTKEY = "F8"


def split(text: str) -> list:
    """
    split string to list without .strip()'ing
    this need for strings like ' word'
    """
    word_list: list[str] = [""]
    while text:
        ch, text = text[0], text[1:]
        if ch == " ":
            word_list += [" ", ""]
        else:
            word_list[-1] += ch
    return word_list


def main() -> None:
    # dirty logic placed here
    cap_text = Capturer.capture()
    if cap_text:
        cap_text = split(cap_text)
        trasleted = [translator.translate(word) for word in cap_text]
        text = "".join(trasleted)
        Capturer.release(text)
    Capturer.clean()


if __name__ == "__main__":
    translator = Translator()
    keyboard.add_hotkey(f"ctrl+{HOTKEY}", main)
    keyboard.wait("esc")
