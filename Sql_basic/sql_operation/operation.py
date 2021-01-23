# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 13:37:55 2021

@author: Arijit
"""

import sqlite3

conn = sqlite3.connect('customers.db')

c = conn.cursor()

## Delete Table if exist ##
c.execute('''
          DROP TABLE customer
          ''')
          
conn.commit()

## Creating Table ##

c.execute('''
          CREATE TABLE customer (
              first_name text,
              last_name text,
              ph_number real)
          ''')
          
          
conn.commit()

## Inserting Table ##

customer_info = [('Arijit' , 'Ghosh' , '9434'),
            ('A' , 'G' , '4567'),]

c.executemany('''
          INSERT INTO customer VALUES (? , ? , ?)
          ''', customer_info)
          
conn.commit()

## Fetching Data ##
c.execute('''
          SELECT * FROM customer
          ''')

print(c.fetchall())

conn.commit()

## Fetching Data where first name is Arijit ##
c.execute('''
          SELECT * FROM customer WHERE first_name = 'Arijit'
          ''')

print(c.fetchall())

conn.commit()

## Fetching first_name where ph number starts with 9 ##

c.execute('''
          SELECT first_name FROM customer WHERE ph_number LIKE '9%'
          ''')
          
print(c.fetchall())

conn.commit()

## Use of ORDER BY ##

c.execute('''
          SELECT * FROM customer WHERE last_name LIKE 'G%' ORDER BY ph_number 
          ''')
          
print(c.fetchall())

conn.commit()

conn.close()