import keyboard
import pyperclip
from time import sleep


"""
For now I import languige directly.
Need to create func to choose from list
"""
import langs.RU as LANG


class Translator:
    def __init__(self, lang=LANG) -> None:
        keyboard.add_hotkey("ctrl+space", self.work)
        self.set_langs(LANG)
        """
        self.native_to_en = lang.EN_TO_NATIVE
        self.eng_to_native = lang.NATIVE_TO_EN
        """

    def set_langs(self, lang) -> None:
        # try: import lang as lang
        try:
            self.native_to_en = LANG.EN_TO_NATIVE
            self.eng_to_native = LANG.NATIVE_TO_EN
        except NameError:
            raise NoDictionary("No dictionary file!")

    def translate(self, text: str) -> str:
        result = ""
        for ch in text:
            if ch in self.native_to_en:
                result += self.native_to_en[ch]
            elif ch in self.eng_to_native:
                result += self.eng_to_native[ch]
            else:
                result += ch
        return result

    def capture(self) -> str:
        keyboard.press_and_release("ctrl+c")
        sleep(0.01)
        return pyperclip.paste()

    def release_and_clean(self) -> None:
        keyboard.press_and_release("ctrl+v")
        sleep(0.01)
        pyperclip.copy("")

    def work(self):
        cap_text = self.capture()
        pyperclip.copy(self.translate(cap_text))
        self.release_and_clean()


class NoDictionary(Exception):
    pass


if __name__ == "__main__":
    translator = Translator()
    keyboard.wait("esc")
