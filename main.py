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
        keyboard.add_hotkey("ctrl+shift", self.work)
        self.set_langs(lang)
        """
        self.native_to_en = lang.EN_TO_NATIVE
        self.eng_to_native = lang.NATIVE_TO_EN
        """

    def set_langs(self, lang) -> None:
        # try: import lang as lang
        try:
            self.native_to_en = lang.EN_TO_NATIVE
            self.eng_to_native = lang.NATIVE_TO_EN
        except NameError:
            raise NoDictionary("No dictionary file!")

    def which_lang(self, text: str) -> dict:
        need_name_for_this_var = a = 0
        for i in text[::-1]:
            if abs(a) > 10:
                break
            elif i not in self.native_to_en:
                a += 1
            elif i not in self.eng_to_native:
                a -= 1
        return self.eng_to_native if a > 0 else self.native_to_en

    def translate(self, text: str) -> str:
        result = ""
        curr_dict = self.which_lang(text)
        for ch in text:
            if ch in curr_dict:
                result += curr_dict[ch]
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
        if cap_text:
            pyperclip.copy(self.translate(cap_text))
        self.release_and_clean()


class NoDictionary(Exception):
    pass


if __name__ == "__main__":
    translator = Translator()
    keyboard.wait("esc")
