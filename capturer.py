import keyboard
import pyperclip
from time import sleep  # time.sleep for some delay between 'keyboard' and 'pyperclip


class Capturer:
    def capture() -> str:
        keyboard.press_and_release("ctrl+c")
        sleep(0.01)
        return pyperclip.paste()

    def release(text: str) -> None:
        pyperclip.copy(text)
        if text[0] == " ":
            keyboard.press_and_release("space")
            sleep(0.01)
        keyboard.press_and_release("ctrl+v")

    def clean():
        sleep(0.01)
        pyperclip.copy("")
