#! /usr/bin/env python2
#! -*- coding: utf-8 -*-

import pysolarized

class Search():

    def __init__(self, title, type):
        self.title = title
        self.type = type
        self.solr = pysolarized.solr.Solr('http://localhost:8983/solr/entities')

    # Index new items
    def add(self):
        self.solr.add([{'title': self.title, 'type': self.type}])
        self.solr.commit()

    # Search item by title
    def query(self):
        results = self.solr.query('%s' % (self.title))
        return results.documents

    # Entity type filter
    def filter(self):
        results = self.solr.query('%s' % (self.title), filters={'type':self.type})
        return results.documents
