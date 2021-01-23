# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 13:26:46 2021

@author: Arijit
"""

import sqlite3

conn = sqlite3.connect('customer_table.db')

c = conn.cursor()

c.execute('''
          CREATE TABLE customer (
          first_name text,
          last_name text,
          email text)
          ''')
         

conn.commit()

conn.close()