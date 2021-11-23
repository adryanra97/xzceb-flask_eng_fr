import unittest

Class Test_french_to_english(unittest.TestCase):
  def test(self):
    self.assertEqual(french_to_english('Bonjour'),'Hello')
    self.assertNotEqual(french_to_english('Bonjour'),'Bonjour')
    
Class Test_english_to_french(unittest.TestCase):
  def test(self):
    self.assertEqual(english_to_french('Hello'),'Bonjour')
    self.assertNotEqual(english_to_french('Hello'),'Hello')
    
unittest.main()
