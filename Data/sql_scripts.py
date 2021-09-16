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

sql_create_contacts_table = '''CREATE TABLE IF NOT EXISTS contacts(
  _id integer PRIMARY KEY AUTOINCREMENT, 
  username text NOT NULL,
  first_name text NOT NULL, 
  last_name text NOT NULL, 
  email text NOT NULL, 
  phone_number text NOT NULL,
  address text, 
  splitwise_token text
  );'''

sql_create_vacations_table = '''CREATE TABLE IF NOT EXISTS vacations(
  _id integer PRIMARY KEY AUTOINCREMENT, 
  name text NOT NULL, 
  start_date text,
  end_date text,
  address text
  );'''

sql_create_guests_table = '''CREATE TABLE IF NOT EXISTS guests(
  _id integer PRIMARY KEY AUTOINCREMENT,
  vacation_id integer,
  guest_id integer,
  FOREIGN KEY(guest_id) REFERENCES contacts(_id),
  FOREIGN KEY(vacation_id) REFERENCES vacations(_id)
);'''

sql_create_todo_table = '''CREATE TABLE IF NOT EXISTS todos(
 todo_id integer PRIMARY KEY AUTOINCREMENT,
 vacation_id integer, 
 contact_id integer, 
 name text,
 description text,
 done integer,
 FOREIGN KEY(vacation_id) REFERENCES vacations(_id),
 FOREIGN KEY(contact_id) REFERENCES contacts(_id)
);'''