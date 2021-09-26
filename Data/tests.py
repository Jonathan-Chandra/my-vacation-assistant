import models
import unittest
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
my_secret = os.getenv("MONGODB_CONNECTION")

class Test_Contact_Is_Equal(unittest.TestCase):
  def test_same_instance(self):
    contact = models.Contact("Test", "first", "last", "test@gmail.com", "444-5554", "1223 Sesame Street", "Token")
    contact1 = contact
    self.assertTrue(contact == contact1)

  def test_same_values(self):
    contact = models.Contact("Test", "first", "last", "test@gmail.com", "444-5554", "1223 Sesame Street", "Token")
    contact1 = models.Contact("Test", "first", "last", "test@gmail.com", "444-5554", "1223 Sesame Street", "Token")
    self.assertTrue(contact == contact1)

  def test_different_values(self):
    contact = models.Contact("Test", "first", "last", "test@gmail.com", "444-5554", "1223 Sesame Street", "Token")
    contact1 = models.Contact("Test Diff", "first", "last", "test@gmail.com", "444-5554", "1223 Sesame Street", "Token")
    self.assertFalse(contact == contact1)

class Test_MongoDB_Connection(unittest.TestCase):
  def test_mongoDB_con(self):
    
    self.assertTrue(True)



if __name__ == '__main__':
  #unittest.main()
  client_string = os.getenv("MONGODB_CONNECTION")
    
  print(my_secret)
  client = MongoClient(client_string)
  try:
    # The ping command is cheap and does not require auth.
    client.admin.command('ping')
  except ConnectionFailure:
    print("Server not available")