sql_create_contacts_table = '''CREATE TABLE IF NOT EXISTS contacts(
  contact_id integer PRIMARY KEY AUTOINCREMENT, 
  first_name text NOT NULL, 
  last_name text NOT NULL, 
  email text NOT NULL, 
  phone_number text NOT NULL,
  address text, 
  splitwise_token text
  );'''

sql_create_vacations_table = '''CREATE TABLE IF NOT EXISTS vacations(
  vacation_id integer PRIMARY KEY AUTOINCREMENT, 
  name text NOT NULL, 
  start_date text,
  end_date text,
  address text
  );'''

sql_create_guests_table = '''CREATE TABLE IF NOT EXISTS guests(
  guest_id integer PRIMARY KEY AUTOINCREMENT,
  FOREIGN KEY(vacation) REFERENCES vacations(vacation_id),
  FOREIGN KEY(guest) REFERENCES contacts(contact_id)
);'''

sql_create_todo_table = '''CREATE TABLE IF NOT EXISTS todos(
 todo_id integer PRIMARY KEY AUTOINCREMENT,
 FOREIGN KEY(vacation) REFERENCES vacations(vacation_id),
 FOREIGN KEY(contact) REFERENCES contacts(contact_id),
 name text,
 description text,
 done integer
);'''