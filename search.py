#! /usr/bin/python2
#! -*- coding: utf-8 -*-

import pysolarized

class Search():

    def __init__(self, title, type):
        self.title = title
        self.type = type
        self.solr = pysolarized.solr.Solr('http://localhost:8983/solr/entities')

    # Indexar itens novos
    def add(self):
        self.solr.add([{'title': self.title, 'type': self.type}])
        self.solr.commit()

    # Busca de item por título
    def query(self):
        results = self.solr.query('%s' % (self.title))
        return results.documents

    # Filtro por tipo de entidade
    def filter(self):
        results = self.solr.query('%s' % (self.title), filters={'type':self.type})
        return results.documents

# TODO: Testes
# TODO: Integrar com ambiente de Continuous Integration
