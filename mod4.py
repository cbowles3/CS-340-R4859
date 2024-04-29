#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 12:08:25 2024

Updated on Sun Apr 7 2024

@author: christopherbo_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB! *EDITED*
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'password'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30037
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
        # Verify connection
        print ("Connection successful")

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True            
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            # When data is found, return result as a list
            readResult = list(self.database.animals.find(data))
            return readResult
        else:
            # When data not found, return an empty list
            raise Exception("Nothing found for that argument.")
            return []
        
# Create method to update a document from a specified MongoDB database
    def update(self, query, data):
        try:
            result = self.database.animals.update_many(query, {'$set': data})
            return {'Success': True, 'Number of documents updated': result.modified_count}
        except Exception as e:
            return {'Success': False, 'Error message': str(e)}
                
    

# Create method to search and remove document(s) from a MongoDB database
    def delete(self, data):
        try:
            result = self.database.animals.delete_many(data)
            return {'Success': True, 'Number of documents deleted': result.deleted_count}
        except Exception as e:
            return {'Success': False, 'Error message': str(e)}
            
        