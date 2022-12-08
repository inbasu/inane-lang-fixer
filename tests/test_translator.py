import os, sys
import unittest

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


import translator


class Test_TRANSLATOR(unittest.TestCase):
    def test_(self):
        demo_translator = translator.Translator()
        self.assertEqual(demo_translator.translate("йцукен"), "qwerty")
        self.assertEqual(demo_translator.translate("qwerty"), "йцукен")
        self.assertEqual(demo_translator.translate("QWERTY"), "ЙЦУКЕН")
        self.assertEqual(demo_translator.translate("qwerty1"), "йцукен1")
        self.assertEqual(demo_translator.translate("555-2368"), "555-2368")
        self.assertEqual(demo_translator.translate("йwerty"), "qцукен")
        self.assertEqual(demo_translator.translate(" qwerty "), " йцукен ")
        self.assertEqual(
            demo_translator.translate('ьнуьфшд"пьфшдюсщь'), "myemail@gmail.com"
        )
        self.assertEqual(demo_translator.translate("   "), "   ")
        self.assertEqual(demo_translator.translate("qwук"), "йцer")


if __name__ == "__main__":
    unittest.main()
