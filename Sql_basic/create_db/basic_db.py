# -*- coding: utf-8 -*-
"""
Spyder Editor

@Created by Arijit
"""

## Importing the sqlite package, which comes in with Python ##

import sqlite3

## Creating connection ##

conn = sqlite3.connect('first_database.db')

## Creating Cursor ##

c = conn.cursor()

## Commiting changes ##

conn.commit()

## Closing connection ##

conn.close()