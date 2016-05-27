Simple Search Engine
===

This is a simple search engine project working with Solr, built in Python 2.7.

Requirements
---
* Python 2.7+

* Solr 6.0.0+

* OpenJDK (because Solr needs it)

Configuration commands
---

`wget http://ftp.unicamp.br/pub/apache/lucene/solr/6.0.0/solr-6.0.0.tgz`

`tar zxvf solr-6.0.0.tgz`

`cd solr-6.0.0`
 
`bin/solr start`

`bin/solr create -c entities`

`cd ..`
 
`git clone https://github.com/cjlcarvalho/SimpleSearchEngine`

`cd SimpleSearchEngine`

`pip2 install -r requirements.txt`

Running the web server
---

`python2 code.py`

After this command, your server will be running in http://0.0.0.0:8080/.

Running the tests
---

`(TO BE DONE)`


