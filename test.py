#-*- coding: UTF-8 -*-
import pymongo

connection = pymongo.MongoClient("localhost",27017)
db = connection.mongodb_tutorial
collectioninfo = db.collection_names()
print collectioninfo
