import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(" "), " ") # test for null input.
    def test2(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test for the translation of the world 'Hello' and 'Bonjour'.
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(" "), " ") # test for null input.
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test for the translation of the world 'Bonjour' and 'Hello'.
        
unittest.main()
