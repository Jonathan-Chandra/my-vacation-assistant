#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Jonathan Chandra"
__copyright__ = "None"
__credits__ = ["Jonathan Chandra"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Jonathan Chandra"
__email__ = "chandra.jonathan@gmail.com"
__status__ = "Prototype"

import datetime
import json


class Contact(object):
  def __init__(self, username: str, first_name: str, last_name: str, email: str, phone_number: str, address: str, splitwise_token:str):
    self.username = username
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.phone_number = phone_number
    self.address = address
    self.splitwise_token = splitwise_token

  def encode(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)

  def decode(self):
    return json.loads(self)


class Vacation(object):
  def __init__(self, vacation_name: str, start_date: datetime, end_date: datetime, address: str):
    self.vacation_name = vacation_name
    self.start_date = start_date
    self.end_date = end_date
    self.address = address

  def encode(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)

  def decode(self):
    return json.loads(self)

class Guest(object):
  def __init__(self, guest_id: int, vacation_id: int, contact_id: int):
    self.guest_id = guest_id
    self.vacation_id = vacation_id
    self.contact_id = contact_id

  def encode(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)
  
  def decode(self):
    return json.loads(self)

class Todo(object):
  def __init__(self, name: str, description: str, done: int):
    self.name = name
    self.description = description
    self.done = done

  def encode(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)
  
  def decode(self):
    return json.loads(self)
