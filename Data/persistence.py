import models
import os
from pymongo import MongoClient

def add_contact(contact: models.Contact):
  client_string = os.getenv("MONGODB_CONNECTION")
  # establing connection
  try:
      client = MongoClient(client_string)
      if models.isValid(contact):
        db = client['vacation-bot'].Contacts
        if db.insert_one(contact):
          client.close()
          return True
        else:
          client.close()
          return False
  except:
    raise Exception("Could not establish connection to MongoDB Server.")
  client.close()
  pass

def get_contact(name: str):
  pass

def get_all_contacts():
  pass

def add_vacation(vacation: models.Vacation):
  pass

def get_vacation_info():
  pass

def add_guest(guest: models.Guest):
  pass

def add_todo(todo: models.ToDo):
  pass

def get_my_todos(info: str):
  pass