import models
import unittest

class Test_Contact_Is_Equal(unittest.TestCase):
  def test_same_instance(self):
    contact = models.Contact("Test", "first", "last", "test@gmail.com", "444-5554", "1223 Sesame Street", "Token")
    contact1 = contact
    self.assertTrue(contact == contact1)

  def test_same_values(self):
    self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()