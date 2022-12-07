import langs.RU as LANG


class Translator:
    def __init__(self, lang=LANG) -> None:
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


class NoDictionary(Exception):
    pass
