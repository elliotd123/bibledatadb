#!/usr/bin/env python3

from bibledatadb import db
from bibledatadb import data

def internal_main():
    print("Creating Database...")
    db.create_database()
    print("Populating Data...")
    data.populate_data()

if __name__ == '__main__':
    internal_main()