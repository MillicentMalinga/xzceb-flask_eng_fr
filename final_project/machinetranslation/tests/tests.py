import unittest
import translator
class TestTranslator(unittest.TestCase):
    def test_nullinputs(self):
        self.assertEqual(translator.english_to_french(''), '')
        self.assertEqual(translator.french_to_english(''), '')

    def test_greetings(self):
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(translator.english_to_french('Hello'), 'Hello')
    
if __name__ == "__main__":
     unittest.main()