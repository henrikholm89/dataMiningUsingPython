#!/usr/bin/env python

import datetime

import pymongo

from pymongo import MongoClient
from prettyprint import prettyprint as pp

class ArticleStore:
  uri = "mongodb://infomine:omitted@linus.mongohq.com:10085/InfoMine"
  db = None
  articles = None
  def connect(self):
    client = MongoClient(self.uri)
    self.db = client.InfoMine

  def insert(self, data):
    article = {"author": None,
      "text": "My first blog post!",
      "tags": ["mongodb", "python", "pymongo"],
      "date": datetime.datetime.utcnow()}
    self.articles = self.db.articles
    article_id = self.articles.insert(article)
    print article_id
  def find_all(self):
    for a in self.articles.find():
      print(a.get("author = None", "text"))

  def find_all_by_iid(self):
    for doc in self.articles.find().sort([
        ('date', pymongo.ASCENDING),
        ('field2', pymongo.DESCENDING)]):
        print(doc)

a = ArticleStore()
a.connect()
a.insert("")
#a.find_all()
a.find_all_by_iid()

"""
connection = pymongo.Connection() # help(pymongo.Connection)
db = connection.test
books = db.books # "books" is a "collection"
book = {"title": "Kongens Fald", "author": "Johannes V. Jensen" }
books.insert(book)
morebooks = [{"title": "Himmerlandshistorier",
"author": "Johannes V. Jensen" },
{"title": "Eventyr", "author": "H. C. Andersen"},
{"title": "Biblen"}]
books.insert(morebooks)



for book in books.find():
  print(book.get("author", "Missing author"))


books.update({"title": "Himmerlandshistorier"}, {"$set": {"isbn": "8702040638"}})
"""

"""
http://www.information.dk/weekend
Kultur
Indland
Udland
Debat
Protokol


No:
telegrammer
fotobloggen
Kortfilmsbloggen
"""
# Articles from 2014 seems to start around ID 483500, which we'll use as threshold
