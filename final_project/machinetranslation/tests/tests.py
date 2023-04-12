import unittest
from translator import frenchToEnglish, englishToFrench

class TestTranslator(unittest.TestCase):
    def test_nullinputs(self):
        self.assertEqual(frenchToEnglish(''), '')
        self.assertEqual(englishToFrench(''), '')

    def test_greetings(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        
    
if __name__ == "__main__":
     unittest.main()