"""
If some one review this code:
is it bad use both word and text as parametrs for string in single class
PLEASE"""


import keyboard
import pyperclip
from time import sleep  # time.sleep for some delay between 'keyboard' and 'pyperclip


"""
For now I import languige directly.
Need to create func to choose from list
"""
import langs.RU as LANG


class Translator:
    def __init__(self, lang=LANG) -> None:
        keyboard.add_hotkey("ctrl+`", self.work)
        self.set_lang(lang)
        """
        ctrl+somekey is necessary becase of 'ctrl+c'/'ctrl+v' conflict
        self.native_to_en = lang.EN_TO_NATIVE
        self.eng_to_native = lang.NATIVE_TO_EN
        """

    def set_lang(self, lang) -> None:
        try:
            self.native_to_en = lang.EN_TO_NATIVE
            self.eng_to_native = lang.NATIVE_TO_EN
        except NameError:
            raise NoDictionary("No dictionary file!")

    def dict_for(self, text: str) -> dict:
        native_vs_en = 0
        for i in text:
            if i not in self.native_to_en:
                native_vs_en += 1
            elif i not in self.eng_to_native:
                native_vs_en -= 1
        if not native_vs_en:
            return dict()
        return self.eng_to_native if native_vs_en > 0 else self.native_to_en

    def translate(self, word: str) -> str:
        result = ""
        curr_dict = self.dict_for(word)
        for ch in word:
            if ch in curr_dict:
                result += curr_dict[ch]
            else:
                result += ch
        return result

    def split(self, text: str) -> list:
        """
        split string to list without .strip()'ing
        this need for strings like ' word'
        """
        sweet_roll = [""]
        while text:
            ch, text = text[0], text[1:]
            if ch == " ":
                sweet_roll.append([" "])
            else:
                sweet_roll[-1] += ch
        return sweet_roll

    def capture(self) -> str:
        keyboard.press_and_release("ctrl+c")
        sleep(0.01)
        return pyperclip.paste()

    def release(self, trasleted) -> None:
        pyperclip.copy("".join(trasleted))
        if not trasleted[0]:
            keyboard.press_and_release("space")
        keyboard.press_and_release("ctrl+v")
        sleep(0.01)

    def work(self) -> None:
        cap_text = self.capture()
        if cap_text:
            cap_text = self.split(cap_text)
            trasleted = [self.translate(word) for word in cap_text]
            self.release(trasleted)
        self.clean_buffer()


class NoDictionary(Exception):
    pass


if __name__ == "__main__":
    translator = Translator()
    keyboard.wait("esc")
