"""
Shipping Receiving Program
python 3.
SQLite3

"""

import sqlite3
from datetime import date
from datetime import datetime
from random import randint
db = sqlite3.connect('Ship-Receive.sqlite3')
c = db.cursor()

def new_table_ship():
	c.execute('''
		CREATE TABLE IF NOT EXISTS ship(id INTEGER PRIMARY KEY, 
			date_time TIMESTAMP, foo INT, description CHAR20)''')
"""
Table Includes:
id - "Auto Incrimenting" id number always chooses next available number
date_time TIMESTAMP format:(YYY-MM-DD HH:MM:SS)
foo INT (placeholder)
description 20 Character String

"""



def get_date():
	print("Input '0' for today")
	year = int(input("Year: "))
	month = int(input("Month: "))
	day = int(input("Day: "))
	hour = int(input("Hour: "))
	minute = int(input("Minute: "))
	now = datetime.now()
	if year == 0:
		year = now.year
	if month == 0:
		month = now.month
	if day == 0:
		day = now.day
	if hour == 0:
		hour = now.hour
	if minute == 0:
		minute = now.minute
	return(year, month, day, hour, minute)


def add_ship_entry():
	
	if count_entries("ship") == 0:
		print('No Rows')
	else:
		c.execute('''SELECT max(id) FROM ship''')
		last_id = c.fetchone()[0]
		new_id = last_id + 1
		print('Input Information for ID# %i' % new_id)

	year, month, day, hour, minute = get_date()

	date_time = datetime(year, month, day, hour, minute)
	print(date_time)
	description = input("Description: ")
	foo = 1

	c.execute('''INSERT INTO ship(date_time, foo, description)
		VALUES(?,?,?)''',(date_time, foo, description))

	db.commit()

def fill_ship():
	for x in range(10):
		year = randint(2016, 2016)
		month = randint(1, 12)
		day = randint(1,28)
		hour = randint(1,12)
		minute = randint(0,59)
		date_time = datetime(year, month, day, hour, minute)
		print(date_time)
		description = "bar"
		foo = 1

		c.execute('''INSERT INTO ship(date_time, foo, description)
			VALUES(?,?,?)''',(date_time, foo, description))

		db.commit()

def new_table_receive():
	null

def print_table(table):
	if table == "ship":
		c.execute(''' SELECT id, date_time, foo, description FROM ship''')
	if table == "receive":
		null
	for row in c:
		print('{0} - {1} : {2}, {3}'.format (row[0], row[1], row[2], row[3]))

def delete_table_entry(table):
	delete_id = input('Enter row ID to delete:')
	print("Row " + delete_id + " Deleted")
	if table == "ship":
		c.execute('''DELETE FROM ship WHERE id=?''',(delete_id,))
	if table == "receive":
		c.execute('''DELETE FROM receive WHERE id=?''',(delete_id,))

def clear_table(table):
	confirm = ""
	confirm = input("To confirm enter 'DROP TABLE " + table + ":")
	if confirm == "DROP TABLE " + table:
		print("New Table " + table)
		if table == "ship":
			c.execute('''DROP TABLE ship''')
			new_table_ship()
		if table == "reveive":
			c.execute('''DROP TABLE receive''')
			new_table_receive()

def count_entries(table):
	if table == "ship":
		c.execute('''SELECT count(*) FROM ship''')
	if table == "receive":
		c.execute('''SELECT count(*) FROM receive''')
	row_count = c.fetchone()[0]
	return row_count

#find entries for today

def find_entries():
	now = datetime.now()
	result_ids = []
	print("Enter Beginning Date")
	beg_year, beg_month, beg_day, beg_hour, beg_minute = get_date()
	print()
	print("Enter End Date")
	end_year, end_month, end_day, end_hour, end_minute = get_date()

	beg_date_time = datetime(beg_year, beg_month, beg_day, beg_hour, beg_minute)
	end_date_time = datetime(end_year, end_month, end_day, end_hour, end_minute)

	c.execute('''SELECT id FROM ship WHERE date_time BETWEEN ? AND ?'''
		,(beg_date_time, end_date_time,))
	result_ids = c.fetchall()
	id_list = [int(i[0]) for i in result_ids]
	if len(id_list) == 0:
		print('no results for your parameters')
	else:
		for x in range(len(id_list)):
			row = id_list[x]
			c.execute('''SELECT id, date_time, foo, description FROM ship WHERE
				id = ?''',(row,))
			print(c.fetchone())

				


#USER INTERFACE
new_table_ship()
target = int(8)
while target != 9:
	target = int(input("\nSelect Option:\n 1.Add Shipping Entry \
			\n 2.Print Shipping Schedule \n 3.Delete Shipping Entry \
			\n 4.Search Date \n 9.Exit \n\n User: " ))
	if target == 1:
		add_ship_entry()
	elif target == 2:
		print_table("ship")
	elif target == 3:
		delete_table_entry("ship")
	elif target == 9:
		print("good-bye")
	elif target == 13:
		clear_table("ship")
	elif target == 4:
		find_entries()
	elif target == 10:
		fill_ship()



db.close()